第十七章代碼搜索

代碼搜索是用於在內部瀏覽和搜索代碼的工具，它由一個前端頁面和各種後端組件組成。就像的許多開發工具一樣，它直接源於代碼庫規模的需求。代碼搜索開始是類似於類型工具的組合，用於帶有排行和的內部代碼外部代碼搜索。通過的整合，它作爲開發人員的關鍵工具的地位得到鞏固，他們增加了交叉引用和跳轉到符號定義的能力。

“”“”“”“”“”“”

這種集成將重點從搜索轉移到瀏覽代碼，後來代碼搜索的發展部分遵循“單擊回答下一個關於代碼的問題”的原則。現在諸如“這個符號在哪裏定義？”，“它在哪裏使用？”、“我如何包含它？”、“它是什麼時候添加到代碼庫中的？”，甚至像“，它消耗多少週期？”之類的問題。只需單擊一兩次即可得到答案。

與集成開發環境或代碼編輯器相比，代碼搜索針對大規模閱讀、理解和探索代碼的用例進行了優化。爲此，它嚴重依賴基於雲的後端來搜索內容和解決交叉引用。

’

在本章中，我們將更詳細地瞭解代碼搜索，包括員工如何將其作爲開發人員工作流程的一部分，爲什麼我們選擇開發一個單獨的網絡工具來進行代碼搜索，並研究它如何在存儲庫規模下解決搜索和瀏覽代碼問題。

>’>>最初在的個人電腦上運行，當他去度假時，曾經引起全公司的困擾。他去度假時，這臺電腦就被關閉了！這曾經造成了整個公司的困擾。>>>>在年關閉；見。>>>>現在被稱爲，一個提供交叉引用的服務（除其他外）：一個特定的代碼符號的用途例如，一個函數使用完整的構建信息，將其與其他同名的符號區分開來。

代碼搜索用戶界面

“”“”

搜索框是代碼搜索的中心元素（見圖），與搜索一樣，它有“建議”，開發人員可以使用這些“建議”快速導航到文件、符號或目錄。對於更復雜的用例，將返回帶有代碼片段的結果頁面。搜索本身可以被認爲是即時的“在文件中查找”（如命令），具有相關性排行和一些特定於代碼的增強功能，如正確的語法突出顯示、範圍感知以及註釋和字符串文字的感知。搜索也可以在命令行使用，並且可以通過遠程過程調用併入其他工具。當需要事後處理或結果集太大而無法手動檢查時，這會派上用場。

查看單個文件時，大多數標記都是可單擊的，以便用戶快速導航到相關信息。例如，函數調用將鏈接到其函數定義、導入的文件名到實際源文件，或相應錯誤報告註釋中的錯誤。這由等基於編譯器的索引工具提供支持。單擊符號名稱會打開一個面板，其中包含使用該符號的所有位置。同樣，將鼠標懸停在函數中的局部變量上將突出顯示該變量在實現中的所有出現。

“”

代碼搜索還可以顯示文件的歷史記錄，通過與的集成（參見第章）。這意味着查看文件的舊版本，哪些更改影響了它，誰編寫了它們，在中跳轉到它們（參見第章），區分文件的版本，以及經典的“”視圖（如果需要）。甚至可以從目錄視圖中看到已刪除的文件。

員工如何使用代碼搜索？

儘管其他工具中也有類似的功能，但員工仍然大量使用代碼搜索進行搜索和文件查看，並最終用於理解代碼。工程師嘗試使用代碼搜索完成任務被認爲是回答有關代碼的問題，以及重複的意圖變得可見。

>’>>無處不在的代碼瀏覽器鼓勵一個有趣的良性循環：編寫易於瀏覽的代碼。這可能意味着不要把層次嵌套得太深，因爲這需要多次點擊才能從調用站點轉移到實際的實現；使用命名的類型而不是像字符串或整數這樣的通用類型，因爲這樣就很容易找到所有的用法。>>“”>>開發者如何搜索代碼。

哪裏？

“”

大約的代碼搜索試圖解答特定信息在代碼庫中的位置的問題；例如，函數定義或配置、的所有用法，或者特定文件在存儲庫中的位置。這些問題非常有針對性，可以通過搜索查詢或遵循語義鏈接（例如“跳轉到符號定義”）來非常精確地回答。此類問題經常出現在重構清理等大型任務中，或者在與其他工程師合作進行項目時。因此，有效解決這些小的知識差距至關重要。

代碼搜索提供了兩種幫助方式：對結果進行排行，以及豐富的查詢語言。排行解決了常見問題，並且可以進行非常具體的搜索（例如，限制代碼路徑，排除語言，僅考慮功能）以處理罕見情況。

“

用戶界面讓同事之間共享代碼搜索結果變得容易。因此，對於代碼審查，你可以簡單地包含鏈接例如，“你是否考慮過使用這個專門的哈希映射：？這對於文檔、錯誤報告和事後分析也非常有用，並且是在中引用代碼的規範方式。甚至可以引用舊版本的代碼，因此鏈接可以隨着代碼庫的發展而保持有效。

什麼？

’

大約四分之一的代碼搜索是典型的文件瀏覽，回答代碼特定部分在做什麼的問題。這些類型的任務通常更具探索性，而不是定位特定的結果。使用代碼搜索來閱讀源代碼，以便在進行更改之前更好地理解代碼，或者能夠理解其他人的更改。

爲了簡化這些類型的任務，代碼搜索引入了調用層次結構瀏覽和相關文件之間的快速導航（例如，在標題、實現、測試和構建文件之間）。通過回答開發人員在查看代碼時遇到的許多問題來理解代碼。

如何做？

最常見的用例大約三分之一的代碼搜索是關於查看其他人如何做某事的示例。通常，開發人員已經找到了特定的（例如，如何從遠程存儲中讀取文件）並希望瞭解如何將應用於特定問題（例如，如何穩健地建立遠程連接並處理某些問題）。代碼搜索還用於首先爲特定問題找到合適的庫（例如，如何有效地計算整數值的指紋），然後選擇最合適的實現。對於這些類型的任務，搜索和交叉引用瀏覽的組合是典型的。

？爲什麼？

與代碼在做什麼有關，關於爲什麼代碼的行爲與預期不同，有更多有針對性的查詢。大約的代碼搜索試圖回答爲什麼要添加某段代碼，或者爲什麼它以某種方式運行的問題。調試過程中經常會出現這樣的問題；例如，爲什麼在這些特定情況下會發生錯誤？

這裏的一個重要功能是能夠在特定時間點搜索和探索代碼庫的確切狀態。在調試生產問題時，這可能意味着使用幾周或幾個月前的代碼庫狀態，而調試新代碼的測試失敗通常意味着使用僅幾分鐘前的更改。兩者都可以通過代碼搜索實現。

誰？什麼時候？

’’“”

大約的代碼搜索試圖回答有關誰或何時引入某段代碼的問題，並與版本控制系統進行交互。例如，可以查看何時引入了特定行（如的“”）並跳轉到相關的代碼審查。這個歷史面板對於尋找最好的人來詢問代碼或審查對它的更改也非常有用。

>“”>>也就是說，考慮到機器生成的更改的提交率，天真的“指責”跟蹤比在更厭惡更改的生態系統中的價值要小。

爲什麼要使用單獨的工具？

在之外，上述大部分實現都是在本地。那麼，爲什麼還需要有另一個工具呢？

規模

’

第一個答案是代碼庫規模太大，以至於完整代碼庫的本地副本（大多數的先決條件）根本不適合單臺機器。即使在這個基本障礙之前，爲每個開發人員構建本地搜索和交叉引用索引也是有成本的，這通常在啓動時降低了開發人員的效率。如果沒有索引，一次性搜索（例如，使用）可能會變得非常緩慢。集中式搜索索引意味着一次性完成這項工作，並且意味着對流程的投資使每個人都受益。例如，代碼搜索索引會隨着每次提交的更改而增量更新，從而能夠以線性成本構建索引。

在正常的網絡搜索中，快速變化的當前事件與變化較慢的項目混合在一起，例如穩定的維基百科頁面。同樣的技術可以擴展到搜索代碼，使索引增加，從而降低成本，並允許對代碼庫的更改立即對所有人可見。提交代碼更改時，只需要對實際觸及的文件進行重新索引，這允許對全局索引進行並行和獨立的更新。

’’

不幸的是，交叉引用索引不能以相同的方式立即更新。增量是不可能的，因爲任何代碼更改都可能影響整個代碼庫，實際上經常會影響數千個文件。需要構建（或至少分析）許多（幾乎所有的）完整二進制文件以確定完整的語義結構。它每天使用大量計算資源（當前頻率）生成索引。即時搜索索引和每日交叉引用索引之間的差異是用戶罕見但反覆出現的問題的根源。

>“”>>相比之下，“每個開發人員在自己的工作空間中都有自己的，並進行索引計算”的模型大致按二次方進行擴展：開發人員每單位時間生成的代碼量大致恆定，因此代碼庫可以線性擴展（即使有固定數量的開發人員）。線性數量的每次都會做線性更多的工作，但這並不是實現良好擴展的祕訣。>>>>使用構建工作流從源代碼中提取語義節點和邊緣。這個提取過程爲每個單獨的生成規則收集部分交叉引用圖。在隨後的階段中，這些局部圖合併爲一個全局圖，並針對最常見的查詢對其表示進行優化（轉到定義，查找所有用法，獲取文件的所有修飾）。每個階段的提取和後處理成本大致與完整構建一樣高；例如，對於，索引的構建在分佈式設置中大約需要六個小時，因此每個開發人員都無法在自己的工作站上構建，成本太高。這就是爲什麼指數每天只計算一次的原因。

零設置全局代碼視圖

’’’

能夠立即有效地瀏覽整個代碼庫意味着很容易找到相關的庫來重用和好的例子來複制。對於在啓動時構建索引的，有一個挑戰是，要有一個小項目或可見範圍來減少啓動時間，並避免像自動完成這樣的工具氾濫而產生噪音。使用代碼搜索，無需設置（例如，項目描述、構建環境），因此無論代碼出現在何處，都可以非常輕鬆快速地瞭解代碼，從而提高開發人員效率。也沒有丟失代碼依賴的危險；例如，在更新時，減少合併和庫版本控制問題。

專業化

’’’

也許令人驚訝的是，代碼搜索的一個優點是它不是。這意味着用戶體驗可以針對瀏覽和理解代碼進行優化，而不是像的大部分內容那樣編輯它（例如，鍵盤快捷鍵、菜單、鼠標點擊，甚至屏幕空間）。例如，由於沒有編輯器的文本光標，每次鼠標單擊符號都可以變得有意義（例如，顯示所有用法或跳轉到定義），而不是作爲移動光標的一種方式。這個優勢是如此之大，以至於開發人員在使用編輯器的同時打開多個代碼搜索選項卡是非常常見的。

與其他開發者工具集成

“”

因爲它是查看源代碼的主要方式，所以代碼搜索是公開源代碼信息的邏輯平臺。它使工具創建者無需爲其結果創建，並確保整個開發人員無需宣傳即可瞭解他們的工作。許多分析會定期在整個代碼庫中運行，它們的結果通常會出現在代碼搜索中。例如，對於許多語言，我們可以檢測“死”（未調用）代碼，並在瀏覽文件時將其標記爲死代碼。

“”

另一方面，指向源文件的代碼搜索鏈接被認爲是其規範的“位置”。這對許多開發工具很有用（見圖）。例如，日誌文件行通常包含日誌記錄語句的文件名和行號。生產日誌查看器使用代碼搜索鏈接將日誌連接回生產代碼。根據可用信息，這可以是指向特定修訂文件的直接鏈接，也可以是具有相應行號的基本文件名搜索。如果只有一個匹配文件，則在相應的行號處打開。否則，將呈現每個匹配文件中所需行的片段。

類似地，堆棧幀被鏈接回源代碼，無論它們是顯示在崩潰報告工具中還是顯示在日誌輸出中，如圖所示。根據編程語言，鏈接將使用文件名或符號搜索。因爲構建崩潰二進制文件的存儲庫的快照是已知的，所以實際上可以將搜索限制在這個版本。這樣，即使相應的代碼後來被重構或刪除，鏈接也會在很長一段時間內保持有效。

編譯錯誤和測試通常還參考代碼位置（例如，測試在文件中行號）。即使對於未提交的代碼，這些也可以鏈接起來，因爲大多數開發都發生在特定的雲可見工作區中，這些工作區可以通過代碼搜索訪問和搜索。

最後，代碼實驗室和其他文檔是指、示例和實現。此類鏈接可以是引用特定類或函數的搜索查詢，當文件結構更改時它們仍然有效。對於代碼片段，最新的實現可以很容易地嵌入到文檔頁面中，如圖所示，而無需使用額外的文檔標記污染源文件。

暴露

代碼搜索將其搜索、交叉引用和語法高亮公開給工具，因此工具開發人員可以將這些功能帶入他們的工具中，而無需重新實現它們。此外，還編寫了插件來提供對編輯器和（例如、和）的搜索和交叉引用。這些插件恢復了由於無法在本地索引代碼庫而損失的一些效率，並提升了一些開發人員的生產力。

規模對設計的影響

’

在上一節中，我們研究了代碼搜索的各個方面，以及爲什麼需要擁有一個單獨的工具來瀏覽代碼。在接下來的部分中，我們會稍微瞭解一下代碼搜索實現的幕後情況。我們首先討論了主要挑戰擴展然後討論了幾種大規模複雜化構建搜索和瀏覽代碼好產品的方式。之後，我們詳細介紹了我們如何應對其中的一些挑戰，以及在構建代碼搜索時做出了哪些權衡。

搜索代碼的最大挑戰是語料庫大小。對於幾兆字節的小型存儲庫，使用搜索的蠻力搜索就可以了。當需要搜索數百兆字節時，一個簡單的本地索引可以將搜索速度提高一個數量級或更多。當需要搜索千兆字節或千兆字節的源代碼時，具有多臺機器的雲託管解決方案可以使搜索時間保持合理。中央解決方案的實用性隨着使用它的開發人員的數量和代碼空間的大小而增加。

>>>因爲查詢是獨立的，所以可以通過擁有更多的服務器來解決更多的用戶。

搜索查詢延遲

’

儘管我們認爲快速響應的對用戶來說更好，但低延遲並不是免費的。爲了證明這一努力的合理性，可以將其與所有用戶節省的工程時間進行權衡。在內部，我們每天在代碼搜索中處理超過一百萬個來自開發人員的搜索查詢。對於一百萬個查詢，每個搜索請求僅增加一秒，就相當於每天大約有名空閒的全職工程師。相比之下，搜索後端可以由大約十分之一的工程師來構建和維護。這意味着每天大約有次查詢（對應於不到名開發人員），僅一秒鐘的延遲參數就可以達到收支平衡點。

’’“”

實際上，生產力損失並不僅僅隨着延遲線性增加。如果延遲低於毫秒，則認爲是響應式的。但僅僅一秒鐘後，開發人員的注意力往往開始轉移。如果再過秒，開發人員很可能會完全切換上下文，這通常被認爲具有很高的生產力成本。讓開發人員保持高效“流動”狀態的最佳方法是將所有頻繁操作的端到端延遲設定在毫秒以下，並投資於相應的後端。

“”

執行大量代碼搜索查詢來導航代碼庫。理想情況下，“下一個”文件只需單擊一下即可（例如，對於包含的文件或符號定義），但對於一般導航，不需要使用經典文件樹，簡單地搜索所需的文件或符號會快得多，理想情況下不需要完全指定它，會爲部分文本提供聯想查詢。隨着代碼庫（和文件樹）的增長，這變得越來越正確。

正常導航到另一個文件夾或項目中的特定文件需要多次用戶交互。使用搜索，只需幾次點擊即可訪問相關文件。爲了使搜索有效，可以將有關搜索上下文的附加信息（例如，當前查看的文件）提供給搜索後端。上下文可以將搜索限制爲特定項目的文件，或者通過優先選擇靠近其他文件或目錄的文件來影響排行。在代碼搜索中，用戶可以預定義多個上下文並根據需要在它們之間快速切換。在編輯器中，打開或編輯的文件被隱式用作上下文，以優先考慮搜索結果的接近程度。

可以將搜索查詢語言的功能（例如，指定文件、使用正則表達式）視爲另一個標準；我們將在本章稍後的權衡部分討論這個問題。

>>>代碼搜索用戶界面也有一個經典的文件樹，所以用這種方式導航也是可以的。

索引延遲

’’

大多數時候，開發人員不會注意到索引何時過期。他們只關心一小部分代碼，即便如此，他們通常也不知道是否有更新的代碼。但是，對於他們編寫或審查相應更改的情況，不同步可能會導致很多混亂。更改是小修復、重構還是全新的代碼片段往往並不重要開發人員只期望一個一致的視圖，例如他們在中爲一個小項目所體驗的。

編寫代碼時，需要對修改後的代碼進行即時索引。當添加新文件、函數或類時，找不到它們是令人沮喪的，並且破壞了用於完善交叉引用的開發人員的正常工作流程。另一個例子是基於搜索和替換的重構。刪除的代碼立即從搜索結果中消失不僅更方便，而且後續重構考慮新狀態也很重要。使用集中式時，如果先前的更改不再是本地修改文件集的一部分，則開發人員可能需要對提交的代碼進行即時索引。

’’“”

相反，有時能夠及時回到之前的代碼快照很有用；換句話說，在事件期間釋放，索引和運行代碼之間的差異可能會是問題，因爲它可以隱藏真正的原因或引入不相關的干擾。這對於交叉引用來說是一個問題，因爲目前在規模上構建索引的技術只需要幾個小時，而且複雜性意味着只保留一個索引的“版本”。儘管可以進行一些修補以使新代碼與舊索引對齊，但這仍然是一個有待解決的問題。

’

谷歌的實現

’

對代碼搜索的特殊實現是針對其代碼庫的獨特特徵量身定製的，上一節概述了我們創建健壯且響應迅速的索引的設計約束。以下部分概述了代碼搜索團隊如何實施並向開發人員發佈工具。

搜索索引

’

由於其龐大的規模，的代碼庫對代碼搜索來說是一個特殊的挑戰。在早期，採用了基於三元組的方法。隨後開源了一個簡化版本。目前，代碼搜索索引大約有的內容，每秒處理大約個查詢，服務器端搜索延遲的中位數小於毫秒，索引延遲的中位數（代碼提交和索引可見性之間的時間）小於秒。

’’

讓我們粗略估計一下使用基於的蠻力解決方案實現此性能所需的資源。我們用於正則表達式匹配的庫以大約秒的速度處理中的數據。給定毫秒的時間窗口，需要個內核來處理的數據。因爲在大多數情況下，簡單的子字符串搜索就足夠了，可以將正則表達式匹配替換爲特殊的子字符串搜索，在某些條件下可以處理大約秒，從而將核心數減少倍。到目前爲止，我們只研究了在毫秒內處理單個查詢的資源需求。如果我們每秒收到個請求，其中個將在毫秒的窗口中同時處於活動狀態，這使我們回到個內核僅用於子字符串搜索。

’’

雖然這個估計忽略了一旦找到一定數量的結果，搜索就會停止，或者文件限制可以比內容搜索更有效地評估，它不需要通信開銷、排行或考慮數萬機器。它很好地展示了所涉及的巨大規模以及爲什麼的代碼搜索團隊不斷投資於改進索引。多年來，我們的索引從最初的基於的解決方案，通過基於自定義後綴數組的解決方案，變爲當前的稀疏解決方案。這個最新的解決方案比蠻力解決方案的效率高出多倍，同時還能夠以極快的速度響應正則表達式搜索。

’“”

我們從基於後綴數組的解決方案轉向基於標記的解決方案的一個原因是利用的主要索引和搜索堆棧。使用基於後綴數組的解決方案，構建和分發自定義索引本身就是一項挑戰。通過利用“標準”技術，我們受益於核心搜索團隊在反向索引構建、編碼和服務方面的進步。即時索引是標準搜索堆棧中存在的另一個功能，在大規模解決它時，它本身就是一個巨大的挑戰。

’’

依賴標準技術是實現簡單性和性能之間的權衡。儘管的代碼搜索實現是基於標準的反向索引，但實際的檢索、匹配和評分都是高度定製和優化的。否則，一些更高級的代碼搜索功能將無法實現。爲了索引文件修訂的歷史，我們提出了一個自定義壓縮方案，在該方案中，索引完整歷史將資源消耗增加了倍。

在早期時候，代碼搜索從內存中提供所有數據。隨着索引大小的增加，我們將倒排索引移至閃存。儘管閃存存儲至少比內存便宜一個數量級，但它的訪問延遲至少要高兩個數量級。因此，在內存中運行良好的索引可能不適合從閃存提供服務。例如，原始的索引不僅需要從閃存中獲取大量的反向索引，而且還需要相當大的索引。使用方案，可以以更大的索引爲代價來減少逆索引的數量及其大小。

爲了支持本地工作空間（與全局存儲庫有一個小的增量），我們有多臺機器進行簡單的暴力搜索。工作區數據在第一次請求時加載，然後通過偵聽文件更改來保持同步。當內存不足時，我們會從機器中刪除最近的工作區。使用我們的歷史索引搜索未更改的文檔。因此，搜索被隱式限制爲工作空間同步到的存儲庫狀態。

>>查閱和

排行

’’’’

對於非常小的代碼庫，排行並沒有帶來太多好處，因爲無論如何也沒有很多結果。但是代碼庫越大，找到的結果就越多，排行也就越重要。在的代碼庫中，任何短子字符串都會出現數千次，甚至數百萬次。如果沒有排行，用戶要麼必須檢查所有這些結果才能找到正確的結果，要麼必須進一步細化查詢，直到結果集減少到幾個文件。這兩種選擇都浪費了開發人員的時間。

“”“”“”

排行通常從評分函數開始，它將每個文件的一組特徵（“信號”）映射到某個數字：分數越高，結果越好。搜索的目標是儘可能高效地找到前個結果。通常，人們區分兩種類型的信號：僅依賴於文檔的信號（“查詢無關”）和依賴於搜索查詢以及它如何匹配文檔的信號（“查詢依賴”）。文件名長度或文件的編程語言將是查詢獨立信號的示例，而匹配是函數定義還是字符串文字是查詢相關信號。

>>>與網絡搜索相比，在代碼搜索查詢中添加更多的字符總是會減少結果集（除了少數通過正則表達式術語的罕見例外）。

查詢獨立信號

’’’’

一些最重要的獨立於查詢的信號是文件視圖的數量和對文件的引用量。文件視圖很重要，因爲它們表明開發人員認爲哪些文件很重要，因此更有可能想要找到。例如，基礎庫中的實用程序函數具有很高的查看次數。庫是否已經穩定並且不再更改或者庫是否正在積極開發都無關緊要。該信號的最大缺點是它創建的反饋迴路。通過對經常查看的文檔進行更高的評分，開發人員查看它們的機會增加，並降低了其他文檔進入前的機會。這個問題被稱爲利用與探索，存在各種解決方案（例如，高級搜索實驗或訓練數據管理）。在實踐中，過度展示高分項目似乎並沒有什麼害處：它們在不相關時被忽略，如果需要通用示例則採用。但是，對於新文件來說，這是一個問題，它們還沒有足夠的信息來獲得良好的信號。

“”’“”

我們還使用文件的引用數量，這與原始頁面排行算法相似，通過將鏈接替換爲大多數語言中存在的各種“包含導入”語句的引用。我們可以將概念向上擴展以構建依賴項（庫模塊級引用）並向下擴展至函數和類。這種全局相關性通常被稱爲文檔的“優先級”。

’

在使用參考進行排行時，必須注意兩個挑戰。首先，你必須能夠可靠地提取參考信息。早期，的代碼搜索使用簡單的正則表達式提取包含導入語句，然後應用啓發式方法將它們轉換爲完整的文件路徑。隨着代碼庫越來越複雜，這種啓發式方法變得容易出錯並且難以維護。在內部，我們用圖中的正確信息替換了這部分。

’

大規模重構，例如開源核心庫，是第二個挑戰。此類更改不會在單個代碼更新中自動發生；相反，它們需要分多個階段推出。通常，引入間接方式，例如隱藏文件的使用移動。這些類型間接降低了移動文件的頁面排行，並使開發人員更難發現新位置。此外，移動文件時文件視圖通常會丟失，從而使情況變得更糟。因爲代碼庫的這種全局重組比較少見（大多數接口很少移動），最簡單的解決方案是在這種過渡期間手動提升文件。（或者等到遷移完成並等待自然過程在其新位置對文件進行升級。）

>’>>這很可能通過使用某種形式的事件作爲信號而得到一定程度的修正，也許可以做一些類似於網絡搜索處理新頁面的事情，但我們還沒有這樣做。

查詢相關信號

’“”

查詢獨立信號可以離線計算，因此計算成本不是主要問題，儘管它可能很高。例如，對於“頁面”排行，信號依賴於整個語料庫，需要類似的批處理來計算。查詢相關信號，即使必須爲每個查詢進行計算，但是計算成本應該很低。這意味着它們僅限於從索引中快速訪問的查詢和信息。

’“””“”

與網絡搜索不同，我們不僅僅匹配令牌。但是，如果存在乾淨的標記匹配（即，搜索詞與帶有某種形式的中斷（例如空格）的內容匹配），則會應用進一步的提升並考慮區分大小寫。這意味着，例如，搜索“”將針對“”的得分高於針對“被任命爲理事會成員”的得分。

’’“”“”“”

爲方便起見，除了實際文件內容外，默認搜索還匹配文件名和限定符號。用戶可以指定特定類型的匹配，但他們不需要。與正常的內容匹配相比，該評分提高了符號和文件名匹配，以反映開發人員的推斷意圖。與搜索一樣，開發人員可以在搜索中添加更多術語以使查詢更加具體。通過文件名提示“限定”查詢是很常見的（例如，“基礎”或“我的項目”）。評分通過提升大部分查詢出現在潛在結果的完整路徑中的結果來利用這一點，將此類結果置於僅包含其內容中隨機位置的單詞的結果之前。

>“”“”“”’>>在編程語言中，像函數這樣的符號經常被定義在一個特定的範圍內，例如類（）或命名空間（）。因此，限定的名稱可能是，這是可以理解的，即使它沒有出現在實際文本中。

恢復

在對文檔進行評分之前，會找到可能與搜索查詢匹配的候選者。這個階段稱爲檢索。因爲檢索所有文檔並不實用，只能對檢索到的文檔進行評分，因此檢索和評分必須協同工作才能找到最相關的文檔。一個典型的例子是搜索類名。根據類的受歡迎程度，它可以有數千種用法，但可能只有一種定義。如果搜索沒有明確限制在類定義中，則在到達具有單個定義的文件之前，可能會停止檢索固定數量的結果。顯然，隨着代碼庫的增長，問題變得更具挑戰性。

檢索階段的主要挑戰是在大量不那麼關聯的文件中找到少數高度相關的文件。一種效果很好的解決方案稱爲補充檢索。這個方法是將原始查詢重寫爲更專業的查詢。在我們的示例中，這意味着補充查詢會將搜索限制爲僅定義和文件名，並將新檢索到的文檔添加到檢索階段的輸出中。在補充檢索的簡單實現中，需要對更多文檔進行評分，但獲得的額外部分評分信息可用於全面評估檢索階段中最有希望的文檔。

結果多樣性

搜索的另一個方面是結果的多樣性，這意味着試圖在多個類別中給出最好的結果。一個簡單的例子是爲一個簡單的函數名提供和匹配，而不是用一個或另一個填充結果的第一頁。

’’’’

當用戶的意圖不明確時，這一點尤其重要。多樣性的挑戰之一是有許多不同的類別如函數、類、文件名、本地結果、用法、測試、示例等結果可以分組，但沒有很多中的空間來顯示所有結果甚至所有組合的結果，這是不可取的。的代碼搜索在這方面的表現不如網絡搜索，但建議結果的下拉列表（如網絡搜索的自動完成）經過調整，可以匹配用戶的當前工作區。

選擇的權衡

’

在這麼大量級的代碼庫中實現代碼搜索並保持其響應速度需要做出各種權衡。這些將在下一節中註明。

完整性：倉庫頭部

’

我們已經看到，更大的代碼庫會對搜索產生負面影響；例如，更慢且更昂貴的索引、更慢的查詢和更嘈雜的結果。是否可以通過犧牲完整性來降低這些成本？換句話說，將一些內容排除在索引之外？答案是肯定的，但要謹慎。非文本文件（二進制文件、圖像、視頻、聲音等）通常不適合人類閱讀，而是從文件名中刪除。因爲它們很大，所以可以節省大量資源。更邊緣的情況涉及生成的文件。由於混淆和結構丟失，它們對人類來說幾乎是不可讀的，因此將它們從索引中排除通常是一個很好的權衡，以完整性爲代價減少索引資源和噪音。根據經驗，數兆字節的文件很少包含與開發人員相關的信息，因此排除極端情況可能是正確的選擇。

’

但是，從索引中刪除文件有一個很大的缺點。對於依賴代碼搜索的開發人員，他們需要能夠信任它。不幸的是，如果刪除的文件一開始沒有被索引，通常不可能就特定搜索的不完整搜索結果提供反饋。給開發人員帶來的混亂和生產力損失是爲節省的資源付出的高昂代價。即使開發人員完全意識到這些限制，如果他們仍然需要執行搜索，他們也會以一種臨時且容易出錯的方式進行。鑑於這些罕見但潛在的高成本，我們選擇在索引過多方面犯錯，具有比較高的限制，是爲了防止濫用和保證系統穩定性，而不是爲了節省資源。

’

另一方面，生成的文件不在代碼庫中，但通常對索引很有用。雖然目前它們不是，是因爲索引它們需要依賴集成工具和配置，這將是複雜性、混亂和延遲的巨大來源。

完整性：所有結果與最相關結果

正常搜索會犧牲完整性來換取速度，本質上是在賭排行會確保靠前的結果包含所有所需的結果。事實上，對於代碼搜索，排行搜索是更常見的情況，例如用戶正在尋找一個特定的東西，函數定義，可能在數百萬個匹配項中。但是，有時開發人員想要所有結果；例如，查找特定符號的所有地方以進行重構。分析、工具或重構（例如全局搜索和替換）通常需要所有結果。提供所有結果的需求是與搜索之間的根本區別，其中可以採用許多捷徑，例如只考慮排行較高的項目。

’

能夠爲非常大的結果集交付所有結果的成本很高，但我們認爲這是工具所必需的，並且開發人員需要信任結果。然而，因爲對於大多數查詢，只有少數結果是相關的（或者只有少數匹配或只有少數是有用的），我們不想爲了潛在的完整性而犧牲平均速度。

爲了通過一種架構實現這兩個目標，我們將代碼庫拆分爲分片，文件按優先級排行。然後，我們通常只需要考慮每個塊中與高優先級文件的匹配。這類似於網絡搜索的工作方式。但是，如果需要，代碼搜索可以從每個塊中獲取所有結果，以保證找到所有結果。這讓我們能夠解決這兩個用例，而不會因爲不常用的返回大型完整結果集的功能而減慢典型搜索速度。結果也可以按字母順序而不是排行，這對某些工具很有用。

因此，這裏權衡的是更復雜的實現和與更強大的功能，而不是更明顯的延遲與完整性。

>>>對查詢的分析表明，大約三分之一的用戶搜索結果少於個。>>’’“”>>在實踐中，更多的事情發生在幕後，因此響應不會變得異常巨大，開發人員也不會通過搜索幾乎所有內容來破壞整個系統（想象一下搜索字母“”或單個空格）

完整性：分支所有歷史工作區

“”

與語料庫大小相關的是應該索引哪些代碼版本的問題：具體來說，是否應該索引除當前代碼快照（“”）之外的任何內容。如果索引多個文件修訂版，系統複雜性、資源消耗和總體成本會急劇增加。據我們所知，除了當前版本的代碼之外，沒有任何索引任何內容。在查看像或這樣的分佈式版本控制系統時，它們的很多效率都來自對歷史數據的壓縮。但是在構建反向索引時，這些表示的緊湊性會丟失。另一個問題是很難有效地索引圖結構，這是分佈式版本控制系統的基礎。

儘管索引存儲庫的多個版本很困難，但這樣做可以探索代碼如何更改並找到已刪除的代碼。在中，代碼搜索索引（線性）歷史。這意味着可以在代碼的任意快照中搜索代碼庫，查找已刪除的代碼，甚至是某些人創作的代碼。

’

一個大的優點是現在可以簡單地從代碼庫中刪除過時的代碼。以前，代碼經常被移動到標記爲過時的目錄中，以便以後仍然可以找到它。完整的歷史索引還爲在人們的工作空間（未提交的更改）中進行有效搜索奠定了基礎，這些工作空間與代碼庫的特定快照同步。對於未來，歷史索引開闢了在排行時使用有效信號的可能性，例如作者身份、代碼活動等。工作區與全局存儲庫有很大不同：

每個開發人員都可以擁有自己的工作區。工作空間中通常有少量更改的文件。正在處理的文件經常更改。工作空間僅存在相對較短的時間段。

爲了提供價值，工作區索引必須準確反映工作區的當前狀態。

表現力：令牌與子字符串與正則表達式

’

規模的效果受到支持的搜索特徵集的很大影響。代碼搜索支持正則表達式搜索，這增加了查詢語言的功能，允許指定或排除整組術語，並且它們可以用於任何文本，在不存在更深層次的語義工具的情況下，對於文檔和語言特別有用。

’

開發人員還習慣於在其他工具（例如）和上下文中使用正則表達式，因此它們提供了強大的搜索功能，而不會增加開發人員的認知負擔。鑑於創建索引以有效地查詢它們具有挑戰性，因此這種能力是有代價的。有哪些更簡單的選擇？

“”“”“”“”

基於標記的索引（例如：單詞）可以很好地擴展，因爲它只存儲實際源代碼的一小部分，並且得到標準搜索引擎的良好支持。不利的一面是，在處理源代碼時，使用基於標記的索引來有效地實現許多用例是棘手的，甚至不可能有效地實現，這爲標記化時通常被忽略的許多字符附加了意義。例如，在大多數基於標記的搜索中，搜索“”與“”、“”或“”是困難的或不可能的。

標記化的另一個問題是代碼標識符的標記化定義不明確。標識符可以用多種方式編寫，例如、，甚至只是混合在一起而無需任何單詞分隔符。在只記住一些單詞時找到一個標識符對於基於標記的索引來說是一個挑戰。

’“”“”“”“”

標記化通常也不關心字母的大小寫（“”與“”），並且經常會模糊單詞；例如，將“”和“”簡化爲相同的詞幹標記搜索。在搜索代碼時，缺乏精確性是一個嚴重的問題。最後，標記化使搜索空格或其他單詞分隔符（逗號、括號）成爲不可能，即使這在代碼中可能非常重要。

搜索能力的下一步是完整的子字符串搜索，其中可以搜索任何字符序列。提供此功能的一種相當有效的方法是通過基於三元組的索引。在最簡單的形式中，生成的索引大小仍然比源代碼大小小得多。然而，與其他子字符串索引相比，小尺寸的代價是召回準確率相對較低。這意味着查詢速度較慢，因爲不匹配項需要從結果集中過濾掉。這是必須在索引大小、搜索延遲和資源消耗之間找到良好折衷的地方，這在很大程度上取決於代碼庫大小、資源可用性和每秒搜索量。

’

如果子字符串索引可用，很容易擴展它以允許正則表達式搜索。基本思想是將正則表達式自動機轉換爲一組子字符串搜索。這種轉換對於三元索引很簡單，並且可以推廣到其他子字符串索引。因爲沒有完美的正則表達式索引，所以總是可以構建導致暴力搜索的查詢。然而，鑑於只有一小部分用戶查詢是複雜的正則表達式，在實踐中，通過子字符串索引的近似效果非常好。

>>>還有其他的類似方式，如建立前綴後綴索引，但一般來說，它們在搜索查詢中提供的表達能力較低，同時仍有較高的複雜性和索引成本。>“”>>，用三元索引進行正則表達式匹配或谷歌代碼搜索的工作原理。

結論

’

代碼搜索從的有機替代品發展成爲提高開發人員生產力的核心工具，並在此過程中利用了的網絡搜索技術。不過，這對你意味着什麼？如果你在一個很容易融入你的的小項目上，可能不多。如果你負責在更大的代碼庫上提高工程師的生產力，那麼你可能會獲得一些見解。

’’“”

最重要的一點可能是顯而易見的：理解代碼是開發和維護代碼的關鍵，這意味着投資在理解代碼上將產生可能難以衡量但實實在在的紅利。我們添加到代碼搜索中的每個功能都被開發人員用來幫助他們完成日常工作（誠然，其中一些功能比其他功能更多）。兩個最重要的功能，集成（即添加語義代碼理解）和查找工作示例，也與理解代碼最明顯相關（例如，查找代碼或查看代碼如何更改）。就工具影響而言，沒有人使用他們不知道存在的工具，因此讓開發人員瞭解可用工具也很重要在谷歌，它是“”培訓的一部分，即新人的入職培訓和聘請的軟件工程師培訓。

對你而言，這可能意味着爲設置標準索引配置文件、分享有關的知識、運行或設置一些自定義索引工具，例如代碼搜索。無論你做什麼，它幾乎肯定會被使用，而且使用得更多，而且使用的方式與你預期的不同你的開發人員將從中受益。

內容提要

’“”

幫助你的開發人員理解代碼可以大大提高工程生產力。在，這方面的關鍵工具是代碼搜索。作爲其他工具的基礎以及作爲所有文檔和開發工具連接到的中心標準位置，代碼搜索具有附加價值代碼庫的龐大規模使得定製工具（例如，與或的索引不同）成爲必要。作爲一種交互式工具，代碼搜索必須快速，允許“問題和回答”的工作流程。預計在各個方面都有低延遲：搜索，瀏覽和索引。只有當它被信任時纔會被廣泛使用，並且只有當它索引所有代碼、給出所有結果並首先給出期望的結果時纔會被信任。但是，只要瞭解其侷限性，較早的、功能較弱的版本既有用又可以使用。