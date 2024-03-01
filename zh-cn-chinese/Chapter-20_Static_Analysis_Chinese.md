第二十章靜態分析

“”“”

靜態分析是指通過程序分析源代碼來發現潛在的問題，例如、反模式和其他無需執行程序就能發現的問題。“靜態”具體是指分析源代碼，而不是運行中的程序（即“動態”分析）。它可以在代碼被合入生產環境前發現，例如，可以識別溢出的常量表達式、永遠不會運行的測試用例或日誌字符串的無效格式化導致運行崩潰的問題。但靜態分析的作用不只是查找。通過對代碼的靜態分析，我們編寫了最佳實踐，幫助推進代碼使用最新接口和減少技術債，這些分析的例子包括：校驗是否遵循命名規範；標記已棄用但仍然使用的接口；簡化表達式以提高代碼可讀性。靜態分析也是棄用某個接口時不可或缺的工具，它可以防止將代碼庫遷移到新接口時出現“倒退”現象（參見第章，指被調用系統不斷遷移舊接口到新接口，而其他系統不斷的調用棄用接口而不調用新接口）。我們還發現靜態分析檢查可以對開發人員起到啓發和約束作用，可以防止開發人員寫出反模式的代碼。

’

本章我們將介紹如何進行有效的靜態分析，包含我們在瞭解到的一些關於靜態分析工作的經驗和我們在靜態分析工具和流程中的最佳實踐。

>>>查閱。>>>>等人，。構建一個程序分析生態系統，國際軟體工程會議（），年月。>>>>關於靜態分析理論，一個很好的學術參考資料是。等人，《程序分析原理》

有效靜態分析的特點

儘管幾十年來，靜態分析研究一直專注於開發新的分析技術和具體分析，但提高靜態分析工具的可擴展性和可用性的方法最近纔開始發展。

可擴展性

’

現代軟件變得越來越大，爲了使分析工具在不減慢軟件開發過程的情況下及時生效，必須有效地解決擴展性問題。對來說，分析工具需要滿足數十億行代碼庫的規模。爲此，分析工具是分片和增量分析的，即不是分析整個大型項目，而是將分析重點放在受待處理代碼變更影響的文件上，並且通常僅顯示已編輯文件或行的分析結果。擴展也有好處：因爲我們的代碼庫非常大，這樣做在尋找時容易的多。除了確保分析工具可以在大型代碼庫上運行之外，還需要必須擴大可分析的數量和種類。分析器是在整個公司範圍內徵求的。靜態分析可擴展性的另一個組成部分是確保過程是可擴展的，爲此，靜態分析基礎架構通過直接向相關工程師展示分析結果來避免造成分析瓶頸。

可用性

“”“”

考慮可用性時，重要的是要考慮靜態分析工具用戶的成本效益權衡。這種”成本”可能是開發時間或代碼質量。修復靜態分析警告可能會引入錯誤的。對於不經常被修改的代碼，爲什麼要修復在生產中運行良好的代碼？例如，通過添加對死代碼從未被運行過的代碼的調用來修復硬編碼警告，可能會導致未經測試（可能有錯誤）的代碼突然運行。這種做法收益不明確，但是成本可能很高。出於這個原因，我們通常只關注新引入的警告，代碼中的現有問題通常只在特別重要（安全問題、重大錯誤修復等）時才值得修復。關注新引入的警告（或修改行上的警告）也意味着查看警告的開發人員具有最相關的上下文和背景。

此外，開發人員的時間很寶貴，要對分析報告進行分類或修復突出問題所花費的時間與特定分析提供的收益進行權衡。如果分析可以節省時間（例如，通過提供可以自動應用於相關代碼的修復），則成本就會下降。任何可以自動修復的東西都應該自動修復。我們還嘗試向開發人員展示實際上對代碼質量有負面影響的問題的報告，這樣他們就不會浪費時間費力地處理不相關的分析結果。

爲了進一步降低查看靜態分析結果的成本，我們將重點放在平滑的開發人員工作流程集成上。在一個工作流中同質化所有內容的另一個優勢是，一個專門的工具團隊可以隨着工作流和代碼一起更新工具，從而允許分析工具與源代碼同步發展。

我們在使靜態分析具有可擴展性和可用性方面所做的這些選擇和權衡，是從我們對三個核心原則的關注中產生的，我們將在下一節中闡述這三個原則作爲經驗教訓。

靜態分析工作中的關鍵工作

’

我們在瞭解到瞭如何用好靜態分析工具的三個關鍵點。讓我們在下面的小節中看看它們。

關注開發者的幸福感

’’

我們提到了一些試圖節省開發人員時間並降低與靜態分析工具交互成本的方法，我們還跟蹤分析工具的性能。如果你不衡量這點，你就無法解決問題。我們只部署誤報率較低的分析工具（稍後將詳細介紹）。我們還積極徵求開發人員對靜態分析結果的實時反饋並採取行動，在靜態分析工具用戶和開發人員之間形成反饋閉環，創造一個良性循環，建立了用戶信任，藉此改進我們的工具。用戶信任對於靜態分析工具的成功至關重要。

“”“”

對於靜態分析，“漏報（）”是指一段代碼包含分析工具找到的問題，但該工具忽略了該問題，“誤報（）”是指工具錯誤地將代碼標記爲存在問題。一般來說，靜態分析工具的研究側重於減少誤判；實踐中，開發者是否真正想要使用工具取決於誤報率是否很低誰願意在數百個虛假報告中費力尋找一些真實的報告？

“”“”

此外，用戶感知是誤報率的一個關鍵方面。如果靜態分析工具產生的警告在技術上是正確的，但被用戶誤解爲誤報（例如，由於告警消息混亂），用戶的反應將與這些警告實際上是誤報一樣。類似地，技術上正確但在大局中不重要的警告也會引發同樣的反應。我們將用戶感知的誤報率稱爲“有效誤報率”。如果開發者在看到問題後沒有采取積極的行動，那麼問題就是“有效的誤報（）”，這意味着，如果一個分析錯誤地報告了一個問題，但開發人員仍然樂於進行修復，以提高代碼的可讀性或可維護性，那麼這就不是一個有效的誤報。例如，我們有一個分析，它標記了這樣一種情況：當開發人員實際上打算調用時，開發人員在哈希表（相當於）上調用方法，即使開發人員正確地打算檢查值，調用反而更清晰。同樣，如果分析報告了一個實際的故障，但開發人員不瞭解故障，因此沒有采取任何行動，這就是一個有效的誤報。

>>>請注意，有一些特定的分析，審查員可能願意容忍更高的誤報率：一個例子是識別關鍵問題的安全分析。

使靜態分析成爲核心開發人員工作流程的一部分

在，我們通過與代碼審查工具集成，將靜態分析集成到核心工作流中。基本上提交的所有代碼在提交之前都會經過審查，因爲開發人員在發送代碼供審查時已經改變了心態，所以靜態分析工具建議的改進可以在沒有太多幹擾的情況下進行。代碼審查集成還有其他好處，開發人員通常在發送代碼進行審查後切換上下文，並且在審查員面前被阻止即使需要幾分鐘的時間來運行分析。來自審查員的同行壓力也要求解決靜態分析警告問題，此外，靜態分析可以自動突出常見問題，從而節省審閱者的時間，這有助於代碼評審過程（以及審查員）的規模化。代碼評審是分析結果的最佳選擇。

>>>關於編輯和瀏覽代碼時的額外集成點的更多信息，請參見本章後面的內容。

允許用戶做出貢獻

有許多領域專家，他們的知識可以改進生成的代碼。靜態分析創造了一個利用他們的專業知識並大規模應用的機會，即利用領域專家編寫新的分析工具或在工具中進行單獨檢查。

例如，瞭解特定類型配置文件上下文的專家可以編寫一個分析器來檢查這些文件的屬性。除了領域專家之外，發現並希望防止同類在代碼庫中的任何其他地方再次出現的開發人員也可以提供貢獻。我們專注於構建一個易於插入的靜態分析生態系統，而不是集成一小部分現有工具。我們專注於開發簡單的，可供整個的工程師（不僅僅是分析或語言專家）用來創建分析；例如，重構可以通過指定前後代碼片段來編寫分析器，來達到該分析器期望的效果。

>“”>>，用進行可擴展的、基於實例的重構。重構工具研討會，年。

’：的靜態分析平臺

’

我們的靜態分析平臺是靜態分析的核心部分。是在多次嘗試將靜態分析與開發人員工作流集成的失敗嘗試中誕生的，與之前嘗試的主要區別在於我們堅持不懈地致力於讓只爲用戶提供有價值的結果。與的主要代碼審查工具集成在一起。警告在的差異查看器上顯示爲灰色的註釋框，如圖所示。

’圖的查看，灰色顯示了的靜態分析警告

爲了方便擴展，使用微服務架構。系統將分析請求連同有關代碼更改的元數據發送到分析服務器。這些服務器可以使用該元數據通過基於的文件系統讀取更改中源代碼文件的版本，並且可以訪問緩存的構建輸入和輸出。然後分析服務器開始運行每個單獨的分析器並將輸出寫入存儲層。每個類別的最新結果隨後會顯示在中。因爲分析有時需要等幾分鐘，分析服務器也會發布狀態更新，讓代碼作者和審查員知道分析器正在運行，並在完成後發佈完成狀態。每天分析超過次代碼審查更改，並且通常每秒運行多次分析。整個的開發人員編寫分析（稱爲“分析器”）或爲現有分析貢獻單獨的“檢查”。

“”“”

檢查有四個標準：

易於理解任何工程師都可以輕鬆理解輸出結果。可操作且易於修復與編譯器檢查相比，修復可能需要更多的時間、思考或嘗試，結果應包括有關如何真正修復問題的指導。少於的有效誤報開發人員應該覺得檢查至少在的時間裏指出了實際問題。有可能對代碼質量產生重大影響這些問題可能不會影響正確性，但開發人員應該認真對待它們並有意識地選擇修復它們。

分析儀報告支持種語言，並支持多種分析類型。包括多個分析器，其中大部分來自團隊外部。其中七個分析器本身就是插件系統，具有數百項額外檢查，由的開發人員提供，總體有效的誤報率略低於。

>>>構建一個程序分析生態系統，國際軟件工程會議（），年月。>>“”>>“”通訊期刊

集成工具

集成了許多不同類型的靜態分析工具。

>>>

和擴展了編譯器以分別識別和的反模式。這些反模式可能代表真正的錯誤。例如，考慮以下代碼片段散列類型的字段：

>>>

’

現在考慮的類型是的情況，代碼仍然可以編譯，但是右移是空操作，因此與自身進行異或，不再影響產生的值。我們修復了代碼庫中出現的次該錯誤，同時在中將檢查作爲編譯器錯誤啓用。這樣的例子還有很多。反模式還可以提高代碼的可讀性，例如刪除對智能指針的的冗餘調用。

’

其他分析器展示了語料庫中不同文件之間的關係。如果刪除了代碼庫中其他非代碼位置（例如簽入文檔中）引用的源文件，會發出警告。允許開發人員指定兩個不同文件的部分必須同時更改（如果不是，則發出警告）。的分析器在中的實驗的配置文件上運行，突出顯示常見問題，包括未獲得啓動實驗的正確批准或與影響同一人羣的其他當前正在運行的實驗串擾。分析器對其他服務進行遠程過程調用以提供此信息。

除了源代碼本身之外，一些分析器還可以在該源代碼生成的其他構件上運行；許多項目啓用了二進制大小檢查器，當更改顯着影響二進制大小時會發出警告。

幾乎所有分析器都是面向過程內的，這意味着分析結果基於過程（函數）內的代碼。組合或增量過程間分析技術在技術上是可行的，但需要額外的基礎設施投資（例如，在分析器運行時分析和存儲方法摘要）。

集成反饋渠道

“”“”“”’“”

如上所述，建立分析者和作者之間反饋閉環對於跟蹤和維護開發人員的成幸福感很重要。會在分析結果上顯示單擊“無用”按鈕的選項；此按鈕提供了直接針對分析器作者提交錯誤的選項，說明了爲什麼分析結果信息無用，代碼審查員還可以通過單擊“請修復”按鈕要求變更作者處理分析結果。團隊跟蹤“無用”按鈕點擊率高的分析器，特別是與審閱者要求修複分析結果的頻率有關，如果分析器不能解決問題並改進“無用”，則會禁用分析器。建立和調整這個反饋閉環需要大量工作，但在改進分析結果和更好的用戶體驗方面已經獲得了很大的回報在我們建立清晰的反饋渠道之前，許多開發人員會忽略他們不理解的分析結果

“”

有時修復非常簡單，例如更新分析器輸出的消息文本。我們曾經推出了一個容易出錯的檢查，當太多參數被傳遞給中的類似的函數時，該檢查只接受並且不接受其他說明符）。團隊每週都會收到“無用”的錯誤報告，聲稱分析不正確，因爲格式說明符的數量與參數的數量相匹配所有這些都是由於用戶試圖傳遞除之外的說明符。在團隊將診斷文本更改爲直接聲明該函數僅接受佔位符後，錯誤報告的湧入停止了。改進分析產生的消息可以解釋什麼是錯誤的、爲什麼以及如何在最相關的點上準確地修復它，並且可以對開發人員在閱讀消息時學習一些東西產生影響。

建議的修復

檢查也會在可能的情況下提供修復，如圖所示。

圖中靜態分析修復的例子視圖

’“”“”

當反饋消息不清晰時，自動修復可作爲額外的文檔來源，並且可以降低解決靜態分析問題的成本。修復可以直接應用中，也可以通過命令行工具應用於整個代碼更改。並非所有分析器都提供修復，但很多都有。我們的做法是，優先自動修復樣式問題，例如，通過自動重新格式化源代碼文件的格式化程序。有每種語言的風格指南，規定了各種語言的格式，但指出格式錯誤並不能很好地利用審閱者的時間。審覈者每天點擊數千次“請修復”，作者每天應用自動修復大約次，分析器每天收到次“無用”點擊

按項目定製

“”’

在通過僅顯示高置信度分析結果建立用戶信任基礎後，除了默認啓用的分析器之外，我們還添加了對特定項目運行其他“可選”分析器的能力。比如分析器，此分析器突出顯示潛在的破壞性數據協議緩衝區的格式更改的獨立於語言的數據序列化格式。只有當序列化的數據存儲在某個地方（例如，在服務器日誌中）時，這些更改纔會中斷；沒有存儲序列化數據的項目的協議緩衝區不需要啓用檢查。我們還添加了自定義現有分析器的功能，儘管這種自定義功能很有限，並且默認情況下，許多檢查在代碼庫中統一應用。

“”

一些分析器甚至一開始是可選的，根據用戶反饋進行改進，建立了龐大的用戶羣，然後一旦我們可以利用我們建立的用戶信任，就進入默認狀態。例如，我們有一個分析器，它建議代碼可讀性改進，這些改進通常不會真正改變代碼行爲。用戶最初擔心這種分析過於“嘈雜”，但最終希望獲得更多的分析結果。

這種定製成功的關鍵是專注於項目定製，而不是用戶級定製。項目級定製確保所有團隊成員對其項目的分析結果有一致的看法，並減少一個開發人員試圖解決問題而需要另一位開發人員介紹的情況。

“”

開發的早期，展示了一組相對簡單的樣式檢查器（“”），提供了用戶設置來選擇結果的置信度以顯示和抑制來自特定分析的結果。我們從中刪除了所有這些用戶可定製性，並立即開始收到用戶對煩人的分析結果的投訴。我們沒有重新啓用可定製性，而是詢問用戶爲什麼他們感到惱火，並發現存在各種錯誤和誤報。例如，也在文件上運行，但產生了不正確、無用的結果。我們修復了基礎設施，這樣就不會再發生這種情況了。的誤報率非常高，有用的信號很少，並且通常被編寫的開發人員禁止查看。因爲很少有幫助，所以我們只是禁用了這個。簡而言之，用戶定製導致隱藏的錯誤和抑制反饋。

預提交

“”

除了代碼審查之外，還有其他用於靜態分析的工作流集成點。由於開發人員可以選擇忽略代碼審查中顯示的靜態分析警告，還可以添加一個分析來阻止提交待處理的代碼更改，我們稱之爲預提交檢查。預提交檢查包括對更改的內容或元數據的非常簡單的可定製的內置檢查，例如確保提交消息沒有說“不要提交”或測試文件始終包含在相應的代碼文件中。團隊還可以指定一組測試，這些測試必須通過或驗證特定類別沒有問題。預提交還會檢查代碼是否格式正確。預提交檢查通常在開發人員郵寄更改以供審覈時運行，並在提交過程中再次運行，但它們可以在這些點之間臨時觸發。有關預提交的更多詳細信息，請參閱第章。

“”

一些團隊已經編寫了自己的自定義預提交。這些是在基本預提交集之上的額外檢查，增加了執行比整個公司更高的最佳實踐標準的能力，並添加了特定於項目的分析。這使得新項目比擁有大量遺留代碼的項目（例如）擁有更嚴格的最佳實踐指南。團隊特定的預提交會使大規模變更過程（參見第章）更加困難，因此在變更描述中帶有“”的變更會被跳過。

編譯器集成

“”’’

儘管使用靜態分析阻止提交很好用，但最好在工作流程的早期通知開發人員問題。如果可以的話，我們會嘗試將靜態分析推送到編譯器中。破壞構建是一個不可忽視的警告，但在許多情況下是不可行的。然而，一些分析是高度機械化的，沒有有效的誤報。一個例子是容易出錯的“錯誤”檢查，這些檢查都在的編譯器中啓用，防止錯誤實例再次被引入我們的代碼庫，編譯器檢查需要快速，以免減慢構建速度。此外，我們強制執行這三個標準（編譯器也存在類似的標準）：

可操作且易於修復（只要可能，錯誤應包括可自動應用的建議修復）不產生有效的誤報（分析不應停止生成正確的代碼）報告僅影響正確性而非風格或最佳實踐的問題

’

要啓用新的檢查，我們首先需要清理代碼庫中該問題的所有實例，這樣我們就不會因爲編譯器的發展而破壞現有項目的構建。這也意味着部署新的基於編譯器的檢查的價值必須足夠高，以保證修復它的所有現有實例。有基礎設施，可以通過集羣在整個代碼庫上並行運行各種編譯器（例如和）作爲操作。當編譯器以這種方式運行時，運行的靜態分析檢查必須產生修復以自動進行清理。在準備好並測試了在整個代碼庫中應用修復的待處理代碼更改後，我們提交該更改並刪除所有現有的問題實例。然後我們在編譯器中打開檢查，這樣就不會在不破壞構建的情況下提交問題的新實例。在我們的持續集成系統提交之後，或者在提交之前通過預提交檢查（參見前面的討論）捕獲構建損壞。

’’

我們的目標是永遠不會發出編譯器警告，但是我們不斷的發現開發人員會忽略編譯器警告，要麼啓用編譯器檢查作爲錯誤（並中斷構建），要麼不在編譯器輸出中顯示它。因爲在整個代碼庫中使用相同的編譯器標誌，所以這個決定是全局做出的。無法破壞構建的檢查要麼被抑制，要麼在代碼審查中顯示（例如，通過）。儘管並非的所有語言都有此策略，但最常用的語言都有。和編譯器都已配置爲避免顯示編譯器警告，編譯器將這一點做的很好，因爲在其他語言中會考慮警告的一些事情（例如未使用的變量或包導入），在中是錯誤的。

編輯和瀏覽代碼時分析

’

靜態分析的另一個集成點是集成開發環境。但是，分析需要快速的分析時間（通常小於秒，理想情況下小於毫秒），因此某些工具不適合在這裏集成，此外，還存在確保相同分析在多箇中以相同方式運行的問題。我們還發現的受歡迎程度可能會上升或下降（我們不強制要求單一的），因此集成往往比插入審查過程更混亂。代碼審查還具有顯示分析結果的特定好處。分析可以考慮變更的整個背景，某些對部分代碼點分析可能不準確（例如，在添加調用點之前實現函數時的死代碼分析）。在代碼審查中顯示分析結果也意味着如果代碼作者想忽略分析結果，他們也必須通過審查。也就是說，集成進行適當的分析是顯示靜態分析結果的一個不錯的集成點。

儘管我們主要關注顯示新引入的靜態分析警告或編輯代碼的警告，但對於某些分析，開發人員實際上確實希望能夠在代碼瀏覽期間查看整個代碼庫的分析結果。這方面的例子是一些安全分析。的特定安全團隊希望查看所有問題實例的整體視圖。開發人員還喜歡在計劃清理時通過代碼庫查看分析結果。換句話說，在瀏覽代碼的時候顯示結果是正確的選擇。

總結

靜態分析是一個很好的工具，可以改進代碼庫，儘早發現錯誤，並允許成本更高的過程（如人工審查和測試）聚焦在無法通過機器方式驗證的問題。通過提高靜態分析基礎設施的可擴展性和可用性，我們使靜態分析成爲軟件開發的有效組成部分。

內容提要

關注開發者的幸福感。我們投入了大量精力，在我們的工具中建立分析用戶和作者之間的反饋渠道，並積極調整分析以減少誤報的數量。將靜態分析作爲核心開發人員工作流程的一部分。靜態分析的主要集成點是通過代碼評審，在這裏，分析工具提供修復並讓評審人員參與。然而，我們也在其他方面（通過編譯器檢查、選通代碼提交、在中以及在瀏覽代碼時）集成分析。授權用戶做出貢獻。通過利用領域專家的專業知識，我們可以擴展構建和維護分析工具和平臺的工作。開發人員不斷添加新的分析和檢查，使他們的生活更輕鬆，使我們的代碼庫更好。