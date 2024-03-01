第二十二章大規模變更

思考一下你自己的代碼庫。在一次同步提交中，你可以可靠地更新多少個文件？限制這一數值的因素有哪些？你有沒有試過做出這麼大的改變？在緊急情況下，你能在合理的時間內完成嗎？你的最大提交大小與代碼庫的實際大小相比如何？你將如何測試這種變更？在提交更改之前，需要多少人進行審查？如果它確實被提交，你是否能夠回滾該更改？這些問題的答案可能會讓你大喫一驚（無論是你認爲答案是什麼，還是它們對你的組織來說實際情況怎麼樣）。

’’

在谷歌，我們很久之前就放棄了大型原子變更對代碼庫大規模變更的想法。我們的觀察到的結果是，隨着代碼庫和在其中工作的工程師數量的增加，最大的原子性更改可能會反直覺地減少，運行所有受影響的預提交檢查和測試變得困難，更不用說確保更改中的每個文件在提交前都是最新的了。隨着對代碼庫進行全面更改變得越來越困難，考慮到我們希望能夠持續改進底層基礎設施的普遍願望，我們不得不開發新的方法來推理大規模更改以及如何實現這些更改。

’’’’

在這一章中，我們將談論社會和技術方面的技術，這些技術使我們能夠保持谷歌大型代碼庫的靈活性，並對底層基礎設施的變化做出響應。我們還將提供一些實際例子，說明我們如何以及在何處使用這些方法。儘管你的代碼庫可能不像谷歌的代碼庫，但瞭解這些原則並對其進行局部調整，將有助於你的開發組織在擴大規模的同時，仍然能夠對你的代碼庫進行大規模的變更。

什麼是大規模的變更？

’’

在進一步討論之前，我們應該探討一下什麼是大規模變更（）。根據我們的經驗，是指任何一組邏輯上相關但實際上不能作爲一個單一的原子單元提交的變更。這可能是因爲它涉及到文件太多，以至於底層工具無法一次性提交所有文件，也可能是因爲變化太大，總是會有合併衝突。在很多情況下，是由你的版本庫拓撲結構決定的：如果你的組織使用分佈式或聯邦版本庫集合，在它們之間進行原子修改在技術上可能是不可能的。我們將在本章後面詳細討論原子變更的潛在障礙。

谷歌的幾乎都是使用自動工具生成的。製作的原因各不相同，但修改本身通常分爲幾個基本類別：

使用代碼庫範圍內的分析工具來清理常見的反模式替換已廢棄的庫特性的使用實現底層基礎架構改進，如編譯器升級將用戶從舊系統轉移到新系統

在一個特定的組織中，從事這些特定任務的工程師的數量可能不多，但對於他們的客戶來說，深入瞭解工具和流程是很有用的。就其性質而言，將影響大量的客戶，而工具很容易擴展到只做幾十個相關變更的團隊。

在特定的背後可能有更廣泛的動機。例如，新的語言標準可能會引入一種更有效的習慣用法來完成給定的任務，內部庫接口可能會更改，或者新的編譯器版本可能需要修復新版本標記爲錯誤的現有問題。谷歌的大多數實際上幾乎沒有功能影響：它們往往是爲了清晰、優化或未來兼容性而進行的廣泛文本更新。但從理論上講，並不侷限於這種行爲維護重構類型的變化。

’’’’

在所有這些情況下，在像谷歌這樣規模的代碼庫中，基礎設施團隊可能經常需要改變數十萬個對舊模式或符號的單獨引用。在迄今爲止最大的案例中，我們已經觸及了數百萬個引用，而且我們希望這個過程能夠繼續良好地擴展。一般來說，我們發現儘早且經常投資於工具，以便爲許多從事基礎設施工作的團隊啓用是一種優勢。我們還發現，高效的工具也有助於工程師進行更小的更改。同樣的工具可以有效地更改數千個文件，也可以很好地擴展到數十個文件。

>>>關於原因的一些想法，見第章。>>’“’”’>>在這個聯合的世界裏，我們可以說我們將儘可能快地提交到每個，以保持較小的構建中斷時間！但這種方法實際上不能隨着聯合代碼庫數量的增長而擴展。>>>>關於這種做法的進一步討論，見第章。

誰負責處理？

’

如前所述，構建和管理我們系統的基礎架構團隊負責執行的大部分工作，但工具和資源在整個公司都可用。如果你跳過了第章，你可能會想，爲什麼基礎設施團隊負責這項工作。爲什麼我們不能引入一個新的類、函數或系統，並要求所有使用舊類、函數或系統的人都使用更新後的類、函數或系統？雖然這在實踐中似乎更容易實現，但由於幾個原因，它的擴展性不是很好。

首先，構建和管理底層系統的基礎設施團隊也具備修復數十萬對它們的引用所需的領域知識。使用基礎架構的團隊不太可能具備處理許多此類遷移的背景，並且期望他們重新學習基礎架構團隊已經具備的專業技能在全球範圍內是低效的。集中化處理還允許在遇到錯誤時更快地恢復，因爲錯誤通常屬於一小部分類別，運行遷移的團隊可以有一個正式或非正式的預案來解決這些錯誤。

’

考慮一下做一系列你不理解的半自動化變更中的第一次所需的時間。你可能會花一些時間來閱讀關於更改的動機和性質，找到一個簡單的例子，嘗試遵循所提供的建議，然後嘗試將其應用於你的本地代碼。對組織中的每個團隊重複此操作會大大增加執行的總體成本。通過只讓幾個集中的團隊負責，谷歌將這些成本內部化，並通過使變革更有效地發生來降低成本。

第二，沒有人喜歡沒有資金支持的任務。即使一個新的系統在本質上可能比它所取代的系統更好，這些好處往往分散在整個組織中，因此不太可能重要到讓個別團隊想要主動更新。如果新系統足夠重要，需要遷移到新系統，那麼遷移的成本將由組織的某個部門承擔。集中遷移和核算其成本，幾乎總是比依靠各個團隊的有機遷移更快、更便宜。

此外，擁有需要的系統的團隊有助於調整激勵機制，以確保完成更改。根據我們的經驗，有機遷移不太可能完全成功，部分原因是工程師在編寫新代碼時傾向於使用現有代碼作爲例子。由一個對移除舊系統有既得利益的團隊負責遷移工作，有助於確保遷移工作真正完成。儘管爲一個團隊提供資金和人員配置來運行這類遷移似乎是一項額外的成本，但它實際上只是將沒有資金的授權所產生的外部性內部化，並帶來規模經濟的額外好處。

>“”“”“”’>>我們所說的“無資金授權”是指“外部實體在不平衡薪酬的情況下強加的額外要求”。有點像說每個人都必須在“正式星期五”穿晚禮服，但沒有給你相應的加薪來支付正式着裝的費用。

案例研究：填補坑洞

’’

儘管谷歌的系統用於高優先級遷移，但我們也發現，只要有它們，就可以在我們的代碼庫中提供各種小補丁，沒有它們是不可能的。就像交通基礎設施任務包括修建新道路和修復舊道路一樣，谷歌的基礎設施團隊除了開發新系統和將用戶轉移到新系統之外，還花費大量時間修復現有代碼。

’

例如，在我們歷史的早期，出現了一個模板庫來補充標準模板庫。這個庫被恰當地命名爲谷歌模板庫，它包括幾個頭文件的實現。由於時間上的原因，其中一個頭文件被命名爲，另一個被命名爲（注意文件名中的不同分隔符）。除了讓純粹的一致性主義者發瘋之外，這種差異也導致了生產力的下降，工程師們不得不記住哪個文件使用了哪個分隔符，只有在他們在潛在的漫長的編譯週期中弄錯了纔會發現。

’’

雖然修復這個單一字符的變化看起來毫無意義，尤其是在像谷歌這樣規模的代碼庫中，但我們的工具和流程的成熟度使我們只需花幾周的時間就能完成這個任務。庫的作者可以發現並應用這一變化，而不必打擾這些文件的終端用戶，我們能夠從數量上減少由這一特定問題引起的構建失敗的數量。由此帶來的生產力（和幸福感）的提高超過了做這個改變的時間成本。

’’

隨着在整個代碼庫中進行更改的能力的提高，更改的多樣性也得到了擴展，我們可以做出一些工程決策，知道這些決策在未來並非一成不變。有時，爲填補一些坑洞而付出努力是值得的。

原子變更的障礙

’

在我們討論實際影響的過程之前，我們應該先談談爲什麼很多種類的更改不能原子提交。在理想情況下，所有邏輯更改都可以打包成單個原子提交，可以獨立於其他更改進行測試、審查和提交。不幸的是，隨着版本庫和在其中工作的工程師數量的增加，這種理想變得不太可行。當使用一組分佈式或聯邦版本庫時，即使在小規模下也完全不可行。

技術限制

首先，大多數版本控制系統（）的操作都會隨着更改的大小進行線性擴展。你的系統可能能夠很好地處理小規模提交（例如，幾十個文件的數量），但可能沒有足夠的內存或處理能力來一次性提交成千上萬的文件。在集中式中，提交會阻止其他寫入程序（以及在舊系統中的讀卡器）在處理時使用系統，這意味着大型提交會使系統的其他用戶陷入停滯。

“”“”

簡言之，以原子方式進行大規模更改可能不僅僅是“困難”或“不明智的”：對於給定的基礎設施，這可能根本不可能。將較大的更改拆分爲較小的獨立塊可以繞過這些限制，儘管這會使更改的執行更加複雜。

>>>查閱。

合併衝突

隨着變更規模的增加，合併衝突的可能性也會增加。我們知道的每個版本控制系統都需要更新和合並，如果中央版本庫中存在較新版本的文件，則可能需要手動分析。隨着更改中文件數量的增加，遇到合併衝突的可能性也會增加，並且使用版本庫工作的工程師數量也會增加。

如果你的公司很小，你可能會在週末沒有人做開發的時候，偷偷地修改版本庫中的每個文件。或者你可能有一個非正式的系統，通過在開發團隊中傳遞一個虛擬的（甚至是物理的！）令牌來抓取全局的版本庫鎖。在谷歌這樣的大公司，這些方法是不可行的：任何時候都總有人在對版本庫進行修改。

由於更改中的文件很少，合併衝突的可能性會減小，因此它們更有可能在提交時不會出現問題。該屬性也適用於以下區域。

沒有鬧鬼的墓地

’“”

運營谷歌生產服務的們有一句格言：“沒有鬧鬼墓地”。從這個意義上說，鬧鬼墓地是一個如此古老、遲鈍或複雜的系統，以至於沒有人敢進入它。鬧鬼的墓地往往是被凍結的關鍵業務系統，因爲任何試圖改變它們的行爲都可能導致系統以無法理解的方式失敗，從而使企業付出實實在在的代價。它們構成了真正的生存風險，並可能消耗過多的資源。

’

然而，鬧鬼墓地並不僅僅存在於生產系統中，它們也可以在代碼庫中找到。許多組織都有一些老舊的、未經維護的軟件，它們是由早已離開團隊的人編寫的，並且處於一些重要的創收功能的關鍵路徑上。這些系統也被凍結在時間中，層層疊疊的官僚機構建立起來，防止可能導致不穩定的變化。沒有人想成爲網絡支持工程師，他犯了錯誤！

代碼庫的這些部分是過程的詛咒，因爲它們阻止了大型遷移的完成、它們所依賴的其他系統的退役，或者它們所使用的編譯器或庫的升級。從的角度來看，鬧鬼的墓地阻止了各種有意義的進步。

’’

在谷歌，我們發現這是一個好的、老式的測試。當軟件經過徹底測試後，我們可以對其進行任意更改，並有信心地知道這些更改是否正在中斷，無論系統的時間或複雜性如何。編寫這些測試需要很多努力，但它允許像谷歌這樣的代碼庫在很長一段時間內進化，將鬧鬼軟件墓地的概念交付給它自己的墓地。

異質性

只有當大部分的工作由計算機而不是人類來完成時，才能真正發揮作用。儘管人類可以很好地處理模棱兩可的問題，但計算機依賴於一致的環境將正確的代碼轉換應用到正確的位置。如果你的組織有許多不同的、持續集成（）系統、特定項目的工具或格式化準則，就很難在整個代碼庫中進行全面的更改。簡化環境，增加一致性，對需要在其中活動的人類和進行自動轉換的機器人都有幫助。

例如，谷歌的許多項目都配置了預提交測試，以便在對其代碼庫進行修改之前運行。這些檢查可能非常複雜，從對照白名單檢查新的依賴關係，到運行測試，再到確保變化有相關的。這些檢查中有許多與編寫新功能的團隊有關，但對於來說，它們只是增加了額外的無關的複雜性。

’

我們已經決定採用這種複雜度，例如通過使其成爲我們代碼庫中的標準來運行預提交測試。對於其他不一致性，我們建議團隊在的某些部分接觸到其項目代碼時忽略其特殊檢查。鑑於此類變更對其項目的好處，大多數團隊都樂於提供協助。

測試

’’’

每個變更都應該進行測試（稍後我們將詳細討論這個過程），但是變更越大，實際測試它就越困難。的系統不僅會運行立即受到更改影響的測試，還會運行過渡依賴於更改文件的任何測試。這意味着更改會得到廣泛的覆蓋，但我們還觀察到，在依賴關係圖中，測試距離受影響文件越遠，失敗越不可能是由變化本身造成的。

小的、獨立的更改更容易驗證，因爲每個更改都會影響較小的測試集，但也因爲測試失敗更容易診斷和修復。在個文件的更改中找到測試失敗的根本原因非常簡單；在個文件更改中找到個，就像諺語中說的大海撈針。

’’

這個決定的權衡是，較小的更改將導致相同的測試運行多次，特別是依賴於大部分代碼庫的測試。因爲工程師跟蹤測試失敗所花費的時間比運行這些額外測試所需的計算時間要昂貴得多，所以我們有意識地決定，這是我們願意做出的權衡。這種權衡可能並不適用於所有組織，但值得研究的是，對於你的組織來說，什麼纔是適當的平衡。

>’“”>>這聽起來可能是矯枉過正，而且很可能是。我們正在積極研究爲一個特定的變化確定正確的測試集的最佳方法，平衡運行測試的計算時間成本和做出錯誤選擇的人力成本。

案例研究：測試

’

如今，一個項目中兩位數百分比（到）的變更是的結果是很常見的，這意味着大量的代碼是由全職工作與這些項目無關的人在項目中變更的。如果沒有良好的測試，這樣的工作將是不可能的，谷歌的代碼庫將在自身的壓力下迅速萎縮。使我們能夠系統地將整個代碼庫遷移到較新的，棄用較舊的，更改語言版本，並刪除流行但危險的做法。

“”

即使是一個簡單的單個函數簽名修改，如果在上百個不同的產品和服務的一千多個不同的地方進行，也會變得很複雜。修改寫完後，你需要協調幾十個團隊的代碼審查。最後，在審查通過後，你需要運行儘可能多的測試，以確保變化是安全的。我們說儘可能多，是因爲一個規模不錯的可能會觸發谷歌的每一個測試的重新運行，而這可能需要一段時間。事實上，許多必須計劃好時間，以便在進行的過程中抓住那些代碼違例的下游客戶。

測試可能是一個緩慢而令人沮喪的過程。當一個變更足夠大的時候，你的本地環境幾乎可以肯定會與永久不同步，因爲代碼庫會像沙子一樣在你的工作中移動。在這種情況下，很容易發現自己在運行和重新運行測試，以確保你的變化繼續有效。當一個項目有不穩定的測試或缺少單元測試覆蓋率時，它可能需要大量的人工干預並拖慢整個過程。爲了幫助加快進度，我們使用了一種叫做（測試自動化平臺）的策略。

搭乘列車

對的核心見解是，它們很少相互影響，對於大多數來說，大多數受影響的測試都會通過。因此，我們可以一次測試一個以上的變化，減少執行的測試總數。事實證明，訓練模型對測試非常有效。

列車利用了兩個事實：

往往是純粹的重構，因此範圍非常窄，保留了本地語義。單獨的修改通常比較簡單，而且受到高度審查，所以它們往往是正確的。

’

列車模型還有一個優點，即它同時適用於多個變化，不要求每個單獨的變化都是孤立的。

“”’

列車模式有五個階段，每三小時重新啓動一次：

對於列車上的每個變化，運行個隨機選擇的測試樣本。收集所有通過次測試的變化，並從所有這些變化中創建一個超級變化：”車次。運行所有直接受該組變化影響的測試的聯合。如果足夠大（或足夠底層），這可能意味着運行谷歌資源庫中的每一個測試。這個過程可能需要六個多小時來完成。對於每一個失敗的非漏洞測試，針對每一個進入火車的變化單獨重新運行它，以確定哪些變化導致它失敗。爲每個上火車的變化生成一份報告。該報告描述了所有通過和未通過的目標，可以作爲可以安全提交的證據。

>>>有史以來最大的一系列在三天內從版本庫中刪除了超過億行的代碼。這主要是爲了刪除版本庫中已經遷移到新倉庫的過時部分；但是，你要有多大的信心才能刪除億行的代碼？>>>>通常由工具支持，使查找、製作和審查修改相對簡單。>>“”>>有可能要求提供單次更換的隔離運行，但這是非常昂貴的，而且只在非高峯時段進行。

代碼審查

’’

最後，正如我們在第章中提到的，所有的修改都需要在提交前進行審覈，這個策略甚至適用於。審閱大型提交可能會很乏味、繁重，甚至容易出錯，特別是如果這些修改是手工生成的（我們很快就會討論，這是一個你想避免的過程）。稍後，我們將看看工具化如何在這個領域提供幫助，但對於某些類別的修改，我們仍然希望人類明確地驗證它們是否正確。將一個分解成獨立的片段，使之更容易。

案例研究：到

’’’

從最早期開始，的代碼庫就有一個自毀的智能指針，用於包裝堆分配的對象，並確保在智能指針超出範圍時將其銷燬。這種類型被稱爲，在的代碼庫中被廣泛使用，以確保對象的壽命得到適當的管理。它並不完美，但考慮到該類型首次引入時當時的標準（）的限制，它使程序更加安全。

’

在中，該語言引入了一個新的類型：。嚴格來說比好，但的代碼庫中有超過萬個對的引用，散佈在數百萬個源文件中。向更現代的模式發展需要谷歌內部最大的。

’

在幾個月的時間裏，幾位工程師同時攻克了這個問題。利用谷歌的大規模遷移基礎設施，我們能夠將對的引用改爲對的引用，並慢慢調整，使其行爲更接近於。在遷移過程的高峯期，我們一直在生成、測試和提交超過個獨立的變化，每天觸及超過個文件。今天，在完善了我們的實踐和改進了我們的工具後，我們有時能管理倍的吞吐量。

’’

像幾乎所有的一樣，這個有一個長尾效應，那就是追蹤各種細微的行爲依賴（定律的另一種表現），與其他工程師一起對抗競賽條件，以及使用生成的代碼，而我們的自動化工具是無法檢測到的。我們繼續手動處理這些問題，因爲它們是由測試基礎設施發現的。

在一些廣泛使用的中也被用作參數類型，這使得小的獨立變化變得困難。我們考慮過編寫一個調用圖分析系統，它可以在一次提交中改變及其調用者，但我們擔心由此產生的改變本身太大，無法原子提交。

’

最後，我們能夠最終刪除，首先讓它成爲的類型別名，然後在舊的別名和新的別名之間進行文本替換，最後只是刪除舊的別名。今天，谷歌的代碼庫從使用與生態系統其他部分相同的標準類型中受益，這可能是因爲我們的技術和工具爲。

基礎設施

谷歌已經投資了大量的基礎設施，使成爲可能。這種基礎設施包括用於創建變更、變更管理、變更審查和測試的工具。然而，對最重要的支持可能是圍繞大規模變化和對它們的監督的文化規範的演變。雖然你的組織的技術和社會工具集可能有所不同，但一般原則應該是相同的。

策略和文化

’

正如我們在第章中所描述的那樣，谷歌將其大部分源代碼存儲在單個代碼庫（）中，每個工程師都可以看到幾乎所有這些代碼。這種高度的開放性意味着任何工程師都可以編輯任何文件，並將這些編輯發送給可以批准它們的人進行審查。然而，每一個編輯都有成本，包括生成和審查。

’

從歷史上看，這些成本在某種程度上是對稱的，這限制了單個工程師或團隊可能產生的變更範圍。隨着谷歌工具的改進，以極低的成本生成大量更改變得更加容易，而對於單個工程師來說，給公司內的大量審閱者施加負擔也變得同樣容易。儘管我們希望鼓勵對我們的代碼庫進行廣泛的改進，但我們希望確保在這些改進背後有一些疏忽和深思熟慮，而不是隨意的調整。

’’

最終的結果是爲尋求在谷歌範圍內進行的團隊和個人提供了一個輕量級的審批過程。這個過程由一羣經驗豐富的工程師監督，他們熟悉各種語言的細微差別，並邀請了相關特定變化的領域專家。這個過程的目的不是要禁止，而是要幫助修改者產生儘可能好的修改，從而最大限度地利用谷歌的技術和人力資本。偶爾，這個小組可能會建議清理工作不值得做：例如，清理一個常見的錯別字，但沒有任何辦法防止再次發生。

’’

與這些策略相關的是圍繞的文化規範的轉變。雖然代碼所有者對自己的軟件有責任感很重要，但他們也需要了解是努力擴展軟件工程實踐的重要組成部分。正如產品團隊最熟悉自己的軟件一樣，基礎類庫團隊也知道基礎設施的細微差別，讓產品團隊相信領域專業知識是獲得社會認可的重要一步。作爲這種文化轉變的結果，本地產品團隊已經開始信任作者，讓他們做出與這些作者的領域相關的更改。

’’’

偶爾，本地所有者會質疑作爲更廣泛的的一部分的特定提交的目的，而變更作者會像回應其他審查意見一樣回應這些意見。從社會角度來說，代碼所有者瞭解發生在他們軟件上的變化是很重要的，但他們也意識到他們對更廣泛的並不擁有否決權。隨着時間的推移，我們發現，一個好的和一個可靠的歷史改進記錄已經在整個谷歌產生了對的廣泛認可。

>>>在計算和存儲方面存在明顯的技術成本，但及時審查變更所需的人力成本遠遠超過技術成本。>>“”“”>>例如，我們不希望由此產生的工具被用作一種機制來爭奪評論中“灰色”或“灰色”的正確拼寫。

代碼庫的洞察力

’’“”“”

要進行，我們發現能夠使用傳統工具在文本級別和語義級別上對代碼庫進行大規模分析是非常寶貴的經驗。例如，使用語義索引工具提供了代碼庫各部分之間鏈接的完整地圖，允許我們提出諸如“此函數的調用方在哪裏？”或“哪些類源自此函數？”和類似的工具還提供對其數據的編程訪問，以便可以將它們合併到重構工具中。（更多示例請參見第章和第章。）

我們還使用基於編譯器的索引，在我們的代碼庫上運行基於抽象語法樹的分析和轉換。諸如、或等工具，可以以高度可並行的方式進行轉換，其功能的一部分依賴於這些洞察力。對於較小的變化，作者可以使用專門的、定製的工具、或、正則表達式匹配，甚至是一個簡單的腳本。

’’

無論你的組織使用什麼工具來創建變更，重要的是它的人力與代碼庫成亞線性擴展；換句話說，無論代碼庫的大小，它都應該花費大致相同的人力時間來生成所有需要的變更集合。變更創建工具也應該在整個代碼庫中是全面的，這樣作者就可以確信他們的變更涵蓋了他們試圖修復的所有情況。

’’“”

與本書中的其他領域一樣，對工具的早期投資通常在中短期內獲得回報。根據經驗，我們一直認爲，如果一個變更需要次以上的編輯，工程師學習和執行我們的變更生成工具通常比手動執行該編輯更有效。對於有經驗的“代碼管理員”，這個數字通常要小得多。

變更管理

可以說，大規模變更基礎設施中最重要的部分是一套工具，它將主變更分割成小塊，並獨立管理測試、推送、審查和提交的過程。在谷歌，這個工具被稱爲，我們將在稍後檢查我們的過程時更全面地討論它的使用。在許多方面，不僅僅是一個工具，而是一個在谷歌規模上製作的整個平臺。它提供了一種能力，可以將工具產生的大型綜合修改集分割成較小的分片，這些分片可以被獨立測試、審查和提交。

測試

’

測試是支持大規模變革的基礎設施的另一個重要部分。正如在第章中所討論的，測試是我們驗證我們的軟件將按照預期行爲的重要方法之一。這在應用非人工編寫的更改時尤爲重要。一個強大的測試文化和基礎設施意味着其他工具可以確信這些更改不會產生意外的影響。

’’’

谷歌針對的測試策略與普通更改略有不同，但仍使用相同的底層基礎設施。測試不僅意味着確保大型主分支更改不會導致失敗，而且還意味着可以安全、獨立地提交每個分支。因爲每個分支可以包含任意文件，所以我們不使用標準的基於項目的預提交測試。相反，我們在它可能影響的每個測試的可傳遞閉包上運行每個分支，我們在前面討論過。

編程語言支持

’

谷歌的通常以每種編程語言爲基礎，有些語言比其他語言更容易支持。我們發現，在我們引入新系統並以非原子方式將用戶遷移到這些系統時，諸如類型別名和轉發功能之類的語言功能對於允許現有用戶繼續工作是非常寶貴的。對於缺少這些功能的編程語言，通常很難增量遷移系統。

’’

我們還發現，靜態類型的語言比動態類型的語言更容易進行大規模的自動化修改。基於編譯器的工具以及強大的靜態分析提供了大量的信息，我們可以利用這些信息來建立影響的工具，並在它們進入測試階段之前拒絕無效的轉換。這樣做的不幸結果是，像、和這些動態類型的語言對維護者來說是額外困難的。在許多方面，編程語言的選擇與代碼壽命的問題密切相關：那些傾向於被視爲更注重開發者生產力的編程語言往往更難維護。雖然這不是一個固有的設計要求，但這是目前的技術狀況。

’“”

最後，值得指出的是，自動語言格式化程序是基礎設施的一個重要組成部分。因爲我們致力於優化我們的代碼的可讀性，我們希望確保任何由自動工具產生的變化對即時的審查者和未來的代碼讀者來說都是可理解的。所有的生成工具都將適合於被修改的語言的自動格式化器作爲一個單獨的通道來運行，這樣，針對修改的工具就不需要關注格式化的細節了。將自動格式化，如或，應用到我們的代碼庫中，意味着自動產生的變化將與人類編寫的代碼“合併，減少未來的開發阻力。如果沒有自動格式化，大規模的自動修改就永遠不會成爲谷歌的公認現狀。

>（）>>事實上，最近專門引入了這些類型的語言特性來支持大規模重構（參見

案例研究：

’“”

已經成爲谷歌內部文化的一個重要部分，但它們開始在更廣泛的世界中產生影響。迄今爲止，最著名的案例也許是。

’

年初，庫中的一個漏洞允許任何在其跨類路徑中具有該庫的脆弱版本的應用程序變得容易被遠程執行。這個漏洞被稱爲瘋狂小工具。在其他方面，它允許一個貪婪的黑客對舊金山市交通局的系統進行加密並關閉其運作。由於該漏洞的唯一要求是在其中的某個地方有錯誤的庫，任何依賴於上許多開源項目的東西都會受到攻擊。

爲了解決這個問題，一些有進取心的發起了他們自己版本的程序。通過使用等工具，志願者們確定了受影響的項目，併發送了多個補丁，將其版本的庫升級爲解決的版本。在這個過程中，不是由自動化工具來管理，而是由多個人類來完成這個的工作。

過程

有了這些基礎設施，我們現在可以談談實際製作的過程。這大致可分爲四個階段（它們之間的界限非常模糊）：

授權變更創建分片管理清理

’

通常，這些步驟發生在編寫新系統、類或函數之後，但在設計新系統時記住它們很重要。在谷歌，我們的目標是在設計後繼系統時考慮到從舊系統的遷移路徑，以便系統維護人員能夠自動將用戶轉移到新系統。

授權

“”

我們要求潛在作者填寫一份簡短的文檔，解釋提出變更的原因、其對整個代碼庫的估計影響（即，大變更將產生多少較小的碎片），並回答潛在評審員可能提出的任何問題。這一過程還迫使作者思考他們將如何以常見問題解答和提出的變更描述的形式向不熟悉變更的工程師描述變更。作者還可以從正在重構的的所有者那裏獲得專業審查。

“”’

然後，這個提案被轉發到一個有大約十幾個人的電子郵件列表，這些人對整個過程進行監督。經過討論，委員會就如何推進工作給出反饋。例如，委員會做出的最常見的改變之一是將一個的所有代碼審查交給一個全球批准人。許多第一次做的人傾向於認爲當地的項目負責人應該審查所有的東西，但對於大多數自動來說，讓一個專家瞭解變化的性質並圍繞着正確的審查建立自動化是比較低成本。

在修改被批准後，作者可以繼續推進他們的修改提交。從歷史上看，委員會在批准方面是非常寬鬆的，而且常常不僅批准某一特定的修改，而且批准一系列廣泛的相關修改。委員會成員可以酌情快速處理明顯的修改，而不需要進行充分的審議。

這個過程的目的是提供監督和升級的途徑，而不對的作者過於繁瑣。該委員會還被授權作爲對的擔憂或衝突的升級機構：不同意改變的本地業主可以向該小組提出上訴，該小組可以對任何衝突進行仲裁。在實踐中，很少需要這樣做。

>>>委員會完全拒絕的唯一類型的更改是那些被視爲危險的更改，如將所有空實例轉換爲空，或極低的值，如將拼寫從英式英語更改爲美式英語，或反之亦然。隨着我們在此類變更方面的經驗增加，的成本降低，批准門檻也隨之降低。

變更創建

在獲得必要的批准後，作者將開始製作實際的代碼編輯。有時，這些內容可以全面地生成一個大的全局變化，隨後將被分割成許多小的獨立部分。通常情況下，由於底層版本控制系統的技術限制，修改的規模太大，無法容納在一個全局修改中。

’“”

變更生成過程應儘可能自動化，以便在用戶退回到舊的使用方式或在變更的代碼中出現文本合併衝突時，可以更新父級變更。偶爾，在技術工具無法生成全局變更的罕見情況下，我們也會將變更的生成分給人工（見第頁的案例研究：行動）。儘管這比自動生成變更要耗費更多的人力，但對於時間敏感的應用來說，這使得全局性的變更能夠更快推進。

請記住，我們對代碼庫的可讀性進行了優化，所以無論什麼工具產生的變化，我們都希望產生的變化看起來儘可能的像人類生成的變更。這一要求導致了風格指南和自動格式化工具的必要性（見第章）。

>>>發生這種情況的原因有很多：從現有示例複製和粘貼，提交已經開發了一段時間的更改，或者僅僅依靠舊習慣。>>>>實際上，這是格式的原始工作背後的推理。

分區與提交

’

在全局變更產生之後，作者就開始運行。接收一個大的變化，並根據項目邊界和所有權規則將其分割成可以原子提交的變化。然後，它把每個單獨的分支變化通過一個獨立的測試郵件提交管道。可能是谷歌開發者基礎設施其他部分的重度用戶，所以它對任何給定的的未完成分片數量設置上限，以較低的優先級運行，並與基礎設施的其他部分進行溝通，瞭解它在我們的共享測試基礎設施上產生多少負載是可以接受的。

我們在下面會更多地談論每個分支的具體測試郵件提交過程。

牛與寵物

“”

當提到分佈式計算環境中的單個機器時，我們經常使用牛和寵物的比喻，但同樣的原則可以適用於代碼庫中的變化。

在谷歌，和大多數組織一樣，代碼庫的典型變化是由從事特定功能或錯誤修復的個別工程師手動生成的。工程師們可能會花幾天或幾周的時間來創建、測試和審查一個單一的變化。他們密切瞭解這個變化，當它最終被提交到主資源庫時，他們會感到很自豪。創建這樣的變化就像擁有和養育一隻喜愛的寵物一樣。

’

相比之下，有效地處理需要高度的自動化，併產生大量的單獨變化。在這種環境下，我們發現把特定的修改當作牛來對待是很有用的：無名無姓的提交，在任何時候都可能被回滾或以其他方式拒絕，除非整個牛羣受到影響，否則代價很小。通常情況下，這種情況發生的原因是測試沒有發現的意外問題，甚至是像合併衝突這樣簡單的事情。

“”’’

對於一個寵物提交，不把拒絕放在心上是很難的，但當作爲大規模變革的一部分而處理許多變化時，這只是工作的性質。擁有自動化意味着工具可以更新，並以非常低的成本產生新的變化，所以偶爾失去幾頭牛並不是什麼問題。

測試

’

每個獨立的分支都是通過谷歌的框架來測試的。我們運行每一個依賴於特定變化中的文件的測試，這常常給我們的系統帶來高負荷。

這可能聽起來很昂貴，但實際上，在我們的代碼庫中的數百萬個測試中，絕大多數分支影響的測試不到一千。對於那些影響更多的測試，我們可以將它們分組：首先運行所有分支的所有受影響測試的聯合，然後對於每個單獨的分支，只運行其受影響的測試與那些第一次運行失敗的測試的交集。這些聯合體中的大多數導致代碼庫中的幾乎每一個測試都被運行，因此向該批分支添加額外的變化幾乎是無額外負擔的。

’

運行如此大量的測試的缺點之一是，獨立的低概率事件在足夠大的規模下幾乎是確定出現的。脆弱和易碎的測試，如第章中討論的那些，通常不會損害編寫和維護它們的團隊，對作者來說特別困難。雖然對單個團隊的影響相當小，但分片測試會嚴重影響系統的吞吐量。自動片斷檢測和消除系統有助於解決這個問題，但要確保編寫片斷測試的團隊承擔其成本，這可能是一個持續的努力。

’

根據我們對作爲語義保護、機器生成的更改的經驗，我們現在對單個變化的正確性比對近期有任何不穩定測試更有信心以至於最近不穩定測試現在在通過我們的自動化工具提交時被忽略了。在理論上，這意味着一個單一的分支可能會導致迴歸，而這個迴歸只能由一個不穩定的測試從不穩定到失敗來檢測。在實踐中，我們很少看到這種情況，所以通過人工溝通而不是自動化來處理它。

’

對於任何過程來說，各個分支應該是可以獨立提交的。這意味着它們沒有任何相互依賴性，或者說分支機制可以將相互依賴的變更（比如對頭文件和其實現的變更）歸爲一組。就像其他變化一樣，大規模的更改分支在被審查和提交之前也必須通過項目特定的檢查。

推送審稿人

在通過測試驗證了某項變更是安全的之後，它就會將該變更推送給適當的審查員。在谷歌這樣一個擁有數千名工程師的大公司，審查員的發現本身就是一個具有挑戰性的問題。回顧第九章，版本庫中的代碼是用文件組織的，這些文件列出了對版本庫中特定子樹有批准權限的用戶。使用一個所有者檢測服務來理解這些文件，並根據他們審查特定分片的預期能力來衡量每個所有者。如果一個特定的所有者被證明是沒有響應的，會自動添加額外的審查者，以努力使一個變化得到及時的審查。

’

作爲推送過程的一部分，也運行每個項目的預提交工具，這可能會執行額外的檢查。對於，我們有選擇地禁用某些檢查，例如對非標準的修改描述格式的檢查。儘管這種檢查對於特定項目的個別更改很有用，但它是整個代碼庫中異構性的一個來源，並且會給過程增加很大的阻力。這種異質性是擴展我們流程和系統的障礙，不能指望工具和作者瞭解每個團隊的特殊策略。

’’’

我們還積極地忽略了預先存在問題變更的提交前檢查失敗。在處理單個項目時，工程師很容易修復這些問題並繼續他們原來的工作，但當在的代碼庫中製作時，這種技術無法擴展。本地代碼所有者有責任確保其代碼庫中沒有先前存在的故障，這是他們與基礎設施團隊之間契約的一部分。

審查

’’’“”

與其他更改一樣，由生成的更改預計將通過標準代碼審查過程。在實踐中，我們發現本地業主通常不會像對待普通變更那樣嚴格對待他們太信任產生的工程師了。理想情況下，這些更改會像其他更改一樣被審查，但在實踐中，本地項目業主已經開始信任基礎設施團隊，以至於這些修改往往只被粗略地審查。我們已經開始只把那些需要他們審查的變更發送給本地所有者，而不僅僅是批准權限。所有其他的修改都可以交給全局審批人：擁有所有權的人可以批准整個版本庫的任何修改。

當使用全局審批人時，所有的單個分片都被分配給這個人，而不是分配給不同項目的單個所有者。全局審批人通常對他們正在審查的語言和或庫有特定的知識，並與大規模的變更作者合作，以瞭解預期的變更類型。他們知道變化的細節是什麼，以及它可能存在的潛在失敗模式，並可以相應地定製他們的工作流程。

全局審閱者使用一組單獨的基於模式的工具來審閱每個更改，並自動批准滿足其期望的更改，而不是單獨審閱每個更改。因此，他們只需要手動檢查一小部分由於合併衝突或工具故障而異常的子集合，這使得流程能夠很好地擴展。

提交

最後，提交單個更改。與推送步驟一樣，我們確保更改在最終提交到存儲庫之前通過各種項目預提交檢查。

’

有了，我們能夠在谷歌的所有代碼庫中有效地創建、測試、審查和提交每天數以千計的更改，並使團隊有能力有效地遷移他們的用戶。過去的技術決定，如一個廣泛使用的符號的名稱或一個流行的類在代碼庫中的位置，不再需要是最終決定。

清理

“”’

不同的對完成有不同的定義，從完全刪除舊系統到只遷移高價值的引用，讓舊系統有機地消失。在幾乎所有情況下，重要的是，要有一個系統，防止大規模變革努力消除的符號或系統的額外引入。在谷歌，我們使用和章節中提到的框架，在工程師引入被廢棄對象的新用途時，在審查時進行標記，這已被證明是防止倒退的有效方法。我們在第章中更多地討論了整個廢棄過程。

>>>可悲的是，我們最想有機分解的系統是那些最能適應這種分解的系統。它們是代碼生態系統中的可塑六合環。

總結

’’’

是谷歌軟件工程生態系統的重要組成部分。在設計時，他們開啓了更多的可能性，知道一些設計決策不需要像以前那樣固定。過程還允許核心基礎設施的維護者有能力將谷歌的大量代碼庫從舊的系統、語言版本和庫習語遷移到新的系統，使代碼庫在空間上和時間上保持一致。而這一切都發生在只有幾十名工程師支持數萬名其他工程師的情況下。

’

無論你的組織有多大的規模，你都有理由考慮如何在你的源代碼集合中進行這類全面的改變。不管是出於選擇還是需要，擁有這種能力將使你的組織在擴大規模時有更大的靈活性，同時使你的源代碼隨着時間的推移保持可塑性。

內容提要

過程可以重新思考某些技術決策的不變性。重構的傳統模型在大範圍內被打破。製作意味着養成製作的習慣。