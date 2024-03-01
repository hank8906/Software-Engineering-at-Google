第三章知識共享

’

你的組織對你問題領域的理解比互聯網上的一些隨機的人要好；你的組織應該能解答你的大部分問題。要做到這一點，你需要知道解決問題答案的專家在哪裏和傳播知識的機制，這就是我們將在本章中探討的。這些機制的範圍很廣，從完全簡單的（提問；寫下你所知道的）到系統化，如教程和課程。然而，最重要的是，你的組織需要一種學習文化，這需要創造一種心理上的安全感，允許人們承認自己缺乏知識。

學習的挑戰

’“”“’”“”’

在一個組織內共享專業知識並非易事。沒有強大的學習文化，挑戰隨時出現。谷歌經歷了許多這樣的挑戰，尤其是隨着公司規模的擴大：

缺乏安全感一個環境中，人們不敢在別人面前冒險或犯錯，因爲他們害怕因此受到懲罰。這通常表現爲一種恐懼文化或避免透明的傾向。信息孤島在一個組織的不同部分發生的知識碎片，這些部分沒有相互溝通或使用共享資源。在這樣的環境中，每個小組都形成了自己的做事方式。這往往導致以下情況：信息碎片化每個孤島對整體都有一個不完整的描述。信息重複每個孤島都重新發明了自己的做事方式。信息偏移每個孤島都有自己做同一件事的方法，這些方法在一起協作可能會或可能不會發生衝突。單點故障（）當關鍵信息只能從一個人那裏獲得時，就會出現瓶頸。這與巴士因子有關，在第二章有詳細討論。可能是出於良好的意圖：我們很容易陷入讓我來幫你解決的習慣。但這種方法提高了短期效率（我做起來更快），但代價是長期可擴展性差（團隊從未學會如何做需要做的事）。這種心態也往往導致失敗，組員要麼全會或要麼都不會某方面的知識。要麼全會要麼都不會一羣人被分成了什麼都懂的老人和什麼都不會的新手，幾乎沒有中間地帶。如果專家總是自己做所有的事情，而不花時間通過指導或編寫文檔來培養新的專家，這個問題往往會加劇。在這種情況下，知識和責任繼續在那些已經擁有專業知識的人身上積累，而新的團隊成員或新手則只能自生自滅，提升速度更慢。鸚鵡學舌模仿而不理解。這典型的特徵是在不瞭解其目的的情況下無意識地複製模式或代碼，通常是在假設上述代碼是出於未知原因而需要的情況下。鬧鬼墓地人們避免接觸或改變的地方，通常在代碼中，因爲他們擔心會出問題。與前面提到的鸚鵡學舌不同，鬧鬼墓地的特點是人們因爲恐懼和迷信而避免行動。

’

在本章的其餘部分，我們將深入探討谷歌的工程組織在應對這些挑戰方面成功的策略。

>>>換句話說，我們沒有形成一個單一的全球最大值，而是有一堆的局部最大值。

理念

’

軟件工程可以定義爲多人協作開發多版本程序。人是軟件工程的核心：代碼是重要的產出，但只是構建產品的一小部分。至關重要的是，代碼不是憑空出現的，專業知識也不會憑空出現。每個專家都曾經是菜鳥：一個組織的成功取決於其員工的成長和投入。

’“”

來自專家的個性化、一對一的建議總是寶貴的。不同的團隊的成員有不同的專業領域，因此對於任何給定的問題，最佳的隊友都會有所不同解法。但如果專家休假或調換團隊，原團隊可能會陷入困境。儘管一個人可以爲一對多人提供個性化的幫助，但這並不具有規模，只限於少量的多。

’

另一方面，文檔化的知識不僅可以更好地擴展到團隊，還可以擴展到整個組織。團隊等機制使許多作者能夠與更大的團隊分享他們的專業知識。但是，儘管書面文檔比一對一的對話更具可擴展性，但這種可擴展性也帶來了一些代價：它可能更具普遍性，不太適用於個別學習者的情況，而且隨着時間的推移，還需要額外的維護成本來，保持信息的相關性和實時性。

’

內部知識存在於單個團隊成員所知道的和被記錄下來的東西之間的差距。人類專家知道這些沒有寫下來的東西。如果我們把這些知識記錄下來並加以維護，那麼現在不僅可以讓今天的專家一對一地直接接觸到這些知識，而且可以讓任何能夠找到並查看這些文件的人獲得這些知識。

：內部知識；是指一種僅存在於某個部落中的信息或知識，這些知識不爲外界所知，沒有正式記錄，只能口口相傳。

’’’

因此，在一個神奇的世界裏，如果所有的事情總是完美地、立即地被記錄下來，我們就不需要再諮詢一個人了，對嗎？並非如此。書面知識具有擴展優勢，但有針對性的人力投入也具有擴展優勢。人類專家可以利用他們廣博的知識。他們可以評估哪些信息適用於個人的使用案例，確定文件是否仍然相關，並知道在哪裏可以找到它。或者，如果他們不知道在哪裏可以找到解答，他們知道誰可以解決。

>>>軟件工程。多人開發多版本程序

內部知識和書面知識相互補充。即使是一個擁有完美文檔的專家團隊也需要相互溝通，與其他團隊協調，並隨着時間的推移不斷調整他們的策略。沒有任何一個單一的知識共享方法對於所有類型學習而言都是正確的解決方案，最佳組合的具體內容會根據你的組織而有所不同。團隊知識隨着時間的推移而演變，對你的組織最有效的知識共享方法可能會隨着組織的發展而改變。培訓，專注於學習和成長，並建立自己穩定的專家隊伍：沒有太多的工程專業知識。

搭建舞臺：心理安全

心理安全是促進學習環境的關鍵。

’’

要學習，你必須首先承認有些事情你不明白。我們應該歡迎這種誠實，而不是懲罰它。（谷歌在這方面做得很好，但有時工程師不願意承認他們不懂一些東西。）

學習的一個重要部分是能夠嘗試事情，並感覺到失敗的無責。在一個健康的環境中，人們對提出問題、犯錯和學習新事物感到自在。這是所有谷歌團隊的基本期望；事實上，我們的研究表明，心理安全是有效團隊最重要的組成部分。

導師制

“”’’

在谷歌，我們嘗試在（新的）工程師加入公司時就確定基調。建立心理安全的一個重要方法是爲分配一個導師一個不是他們的團隊成員、經理或技術負責人的人其職責明確包括回答問題和幫助成長。有一個官方指定的導師可以尋求幫助，這對新人來說更容易，也意味着他們不需要擔心會佔用同事太多的時間。

’

導師是在谷歌工作了一年以上的志願者，他可以就使用谷歌基礎設施和了解谷歌文化等方面提供建議。最重要的是，如果被指導者不知道該向誰尋求建議，指導者就會成爲一個安全網。這位導師與被指導者不在同一個團隊，這可以使被指導者在棘手的情況下更放心地尋求幫助。

’’

導師制使學習正規化並促進學習，但學習本身是一個持續的過程。無論是加入組織的新員工還是學習新技術的有經驗的工程師，同事之間總是有機會互相學習。在一個健康的團隊中，隊友們不僅願意回答問題，也願意提出問題：表明他們不知道的東西，並相互學習。

大團體的心理安全

’’

向附近的隊友尋求幫助比接近一大羣大多是陌生的人容易得多。但正如我們所看到的，一對一的解決方案並不能很好地擴展。對於新手來說，出現一個問題並向一大團隊人提問是一種威脅，因爲他們知道自己的問題可能會存在多年。對心理安全的需求在大團隊中被放大了。小組的每個成員都應在創造和維持一個安全的環境中發揮作用，以確保新人自信提出問題，而新晉專家則感到有能力幫助這些新人，而不必擔心他們的答案會受到老專家的攻擊。

實現這種安全和受歡迎的環境的最重要的方法是團體互動是合作性的，而不是對抗性的。表列出了一些推薦的團體互動模式（以及相應的反模式）的例子。

’“”“”

團隊互動模式

推薦的模式（合作型）反模式對抗型基本的問題或錯誤被引導到正確的方向基本的問題或錯誤被挑剔，提出問題的人被責備解釋的目的是爲了幫助提問的人學習解釋的目的是爲了炫耀自己的知識回應親切、耐心、樂於助人回應是居高臨下、尖酸刻薄、毫無建設性的互動是爲尋找解決方案而進行的共同討論”互動是有贏家和輸家的爭論

’

“’’”“”“”“’”

這些反模式可能是無意中出現的：有人可能是想幫忙，但卻意外地居高臨下，不受歡迎。我們發現中心的社交規則在這裏很有幫助：

不要假裝驚訝（什麼？我不相信你不知道堆棧是什麼！）假裝驚訝是心理安全的障礙，使團體成員害怕承認自己缺乏知識。不根據事實迂腐的糾正，往往是爲了譁衆取寵而非糾正。不開小會打斷現有的討論，提供意見，而不投入到對話中。不說微妙的謊言（這太容易了，我奶奶都能做！）小小的偏見表達（種族主義、年齡歧視、恐同症），會使個人感到不受歡迎、不被尊重或不安全。

增長你的知識

知識共享從自己開始。重要的是要認識到，你總是有東西要學。下面的準則可以讓你增加自己的個人知識。

提問

如果你從這一章中只帶走一件事，那就是：永遠學習；保持好奇。

’’“”“”’

我們告訴，提升可能需要個月左右。這個時間的延長對於在谷歌龐大而複雜的基礎設施上的提升是必要的，但它也強化了學習是一個持續、迭代的過程的理念。初學者犯的最大錯誤之一是在遇到困難時不尋求幫助。你可能會想獨自掙扎一下，或者感到害怕你的問題太簡單了。你想：我只是需要在向別人尋求幫助之前更努力地一下。不要落入這個陷阱你的同事往往是最好的信息來源：利用這一寶貴資源。

’’’’“’”

不會有神奇的一天，你突然總是確切地知道在任何情況下該怎麼做總是有更多的東西需要學。在谷歌工作多年的工程師們仍然有一些領域他們覺得自己不知道自己該怎麼做，這沒關係！不要害怕說我不知道那是什麼，你能解釋一下嗎？。把不知道事情當作瞭解新領域的機會，而不是一個恐懼這個未知領域。

’’’

不管你是新加入的團隊還是高級領導者：你應該始終處在一個有東西可學的環境中。如果不是這樣，你就會停滯不前（應該找一個新的環境）。

’’“”“”’’

對於那些擔任領導角色的人來說，塑造這種行爲尤爲重要：重要的是不要錯誤地將資歷等同於無所不知。事實上，你知道的越多，你知道你不知道的就越多。公開提問或表達知識差距，強化了其他人也可以這樣做。

“”’

在接受端，在回答問題時的耐心和善意培養了一種環境，使人們感到安全地尋求幫助。讓人們更容易克服最初對提問的猶豫不決，儘早定下基調：主動徵求問題，讓即使是“瑣碎”的問題也能輕鬆得到答案。雖然工程師們可能會自己摸索出內部知識，但他們不是在真空中工作的。有針對性的幫助可以讓工程師更快地提高工作效率，從而使整個團隊的工作效率更高。

>’>>冒名頂替綜合症在成功人士中並不少見，谷歌也不例外。事實上，本書的大多數作者都患有冒名頂替綜合症。我們承認，對於冒名頂替綜合徵患者來說，對失敗的恐懼可能很難，並且會強化他們避免分道揚鑣的傾向。>>“>>見如何提出好問題。

瞭解背景

“’”

學習不僅僅是瞭解新事物；它還包括對現有事物的設計和實施背後的決策的理解。假設你的團隊繼承了一個已經存在多年的關鍵基礎設施的遺留代碼庫。原作者早就不在了，代碼也很難理解。與其花時間學習現有的代碼，不如從頭開始重寫，這很有誘惑力。但是，不要想着“我不明白”並在那裏結束你的想法，而是深入思考：你應該問什麼問題？

“’”’“’”“’’”

考慮一下的原則：在移除或改變某些東西之前，首先要了解它爲什麼存在。在改造事物的問題上，不同於使事物變形，有一個簡單明瞭的原則；這個原則可能會被稱爲悖論。在這種情況下，存在着某種制度或法律；爲了簡單起見，讓我們說，在一條道路上豎起了柵欄或大門。更現代的改革者興高采烈地走到它面前，說：我看不出來這有什麼用；讓我們把它清除掉吧。對此，更聰明的改革者會很好地回答。如果你看不到它的用途，我當然不會讓你清除它。走吧，好好想想。然後，當你能回來告訴我你確實看到了它的用途時，我纔會允許你銷燬它。

’’’“”’’

這並不意味着代碼不可能缺乏清晰，也不意味着現有的設計模式不可能是錯誤的，但工程師們有一種傾向，即這很糟糕！通常的代碼要快得多，特別是對於不熟悉的代碼、語言或範例。谷歌也不能倖免。尋找和了解背景，特別是對於那些看起來不尋常的決定。在你瞭解了代碼的背景和目的之後，考慮你的改變是否仍然有意義。如果有意義，就繼續做；如果沒有意義，就爲未來的繼任者記錄下你的理由。

’

許多谷歌風格指南明確地包括背景，以幫助讀者理解風格指南背後的理由，而不是僅僅記住一串武斷的規則。更微妙的是，瞭解某條準則背後的理由，可以讓作者做出明智的決定，知道該準則何時不適用，或者該準則是否需要更新。見第章。

擴展你的問題：向社區提問

獲得一對一的幫助是高帶寬的，但規模必然有限。而作爲一個學習者，要記住每一個細節很困難。幫你未來的自己一個忙：當你從一對一的討論中學到一些東西時，把它寫下來。

未來的新來者可能會有和你一樣的問題。也幫他們一個忙，分享你寫下的東西。

’

儘管分享你得到的答案可能是有用的，但尋求更多社區而非個人的幫助也是有益的。在本節中，我們將研究不同形式的社區學習。這些方法中的每一種羣聊、郵件列表和問答系統都有不同的權衡，並相互補充。但它們中的每一種都能使知識尋求者從更廣泛的同行和專家社區獲得幫助，同時也能確保該社區的當前和未來成員都能廣泛獲得答案。

羣聊

’

當你有一個問題時，有時很難從適合的人那裏得到幫助。也許你不確定誰知道答案，或者你想問的人很忙。在這種情況下，羣聊是很好的方式，因爲你可以同時向許多人提出你的問題，並與任何有空的人進行快速的對話。另外，羣聊中的其他成員可以從問題和答案中學習，而且許多形式的羣聊可以自動存檔並在以後進行搜索。

羣聊往往是專門針對主題或團隊。以主題爲導向的羣聊通常是開放的，因此任何人都可以進來問問題。他們傾向於吸引專家，並且可以發展得相當大，所以問題通常會很快得到回答。另一方面，以團隊爲導向的聊天，往往規模較小，並限制成員。因此，他們可能沒有話題驅動型聊天的影響力，但其較小的規模會讓新人感到更安心。

’’

雖然小組聊天對快速提問很有幫助，但它們沒有提供太多的結構化，這會使你很難從一個你沒有積極參與的對話中提取有意義的信息。一旦你需要在羣組之外分享信息，或使其可在以後參考，你應該寫一份文檔或給郵件列表發郵件。

郵件列表

’

谷歌的大多數主題都有一個或的谷歌羣組郵件列表，公司的任何人都可以加入或發送電子郵件。在公共郵件列表上提出問題，很像在羣組聊天中提出問題：這個問題可以傳到很多有可能回答它的人那兒，而且任何關注這個列表的人都可以從答案中學習。但與羣聊不同的是，公共郵件列表很容易與更多人分享：它們被打包成可搜索的檔案，而且電子郵件比羣聊提供更多的結構化。在谷歌，郵件列表也被編入索引，可以被谷歌的內部網搜索引擎發現。

’’

當你找到了你在郵件列表中提出的問題的答案時，你可能會很想繼續你的工作。請不要這樣做你永遠不知道將來什麼時候會有人需要同樣的信息，所以最好將答案發回郵件列表。

’’

郵件列表也有其不足之處。它們很適合處理需要大量背景資料的複雜問題，但對於小組聊天所擅長的快速來回交流來說，它們就顯得很笨拙。一個關於特定問題的線索通常在它活躍的時候是最有用的。電子郵件檔案是不可改變的，而且很難確定在一箇舊的討論主題中發現的答案是否仍然對今天的情況有效。此外，信噪比可能比其他媒介（如正式文件）低，因爲某人在其特定工作流程中遇到的問題可能並不適用於你。

谷歌的電子郵件

’’

谷歌的文化是臭名昭著的以電子郵件爲中心和重度使用電子郵件。谷歌的工程師們每天都會收到數以百計的電子郵件（如果不是更多的話），其中有不同程度的可操作性。新手們需要花好幾天時間來設置電子郵件過濾器，以處理來自他們自動訂閱的羣組的大量通知；有些人乾脆放棄了，放棄追隨最新的郵件。一些羣組將大型郵件列表默認爲每一個討論，而不試圖將信息定向發送給那些可能對其特別感興趣的人；結果，信噪比成爲了一個真正的問題。

’’’’

谷歌默認傾向於基於電子郵件的工作流程。這並不一定是因爲電子郵件是一個比其他通信選項更好的媒介它往往不是而是因爲這是我們的文化所習慣的。當你的組織考慮要鼓勵或投入什麼形式的溝通時，請記住這一點。

：問答平臺

“”

（另一個問題系統）是谷歌內部版本的類似網站，使能夠輕鬆地鏈接到現有或正在進行的代碼，以及討論機密信息。

像一樣，與郵件列表有許多相同的優點，並增加了完善的功能：標記爲有用的答案在用戶界面上被推廣，用戶可以編輯問題和答案，以便隨着代碼和事實的變化保持準確和有用。因此，一些郵件列表已經被所取代，而其他的郵件列表已經演變成更一般的討論列表，不再專注於解決問題。

擴展你的知識：你總是有東西可教的

教學不侷限專家，專業知識也不是一種二元狀態，你要麼是新手，要麼是專家。專業知識是你所知道的一個多維向量：每個人在不同領域都有不同水平的專業知識。這就是爲什麼多樣性是組織的成功至關重要的原因之一：不同的人帶來不同的觀點和專業知識（見第四章）。谷歌工程師以各種方式教授他人，如辦公時間、舉辦技術講座、教授課程、編寫文檔和審查代碼。

固定時間

’’’’’

有時與人交談非常重要，在這些情況下，固定時間是一個很好的解決方案。固定時間是一個定期安排的活動（通常是每週一次），在此期間，一個或多個人可以回答關於某個特定主題的問題。固定時間幾乎從來不是知識共享的首選：如果你有一個緊急的問題，等待下一次會議的答案可能會很痛苦；如果你主持固定時間，它們會佔用時間，需要定期宣傳。也就是說，它們確實爲人們提供了一種與專家當面交談的方式。如果問題還很模糊，工程師還不知道該問什麼問題（比如他們剛開始設計一個新的服務），或者問題是關於一個非常專業的東西，以至於沒有相關的文檔，那麼這就特別有用。

技術講座和課程

“”“”

谷歌擁有強大的內部和外部技術講座和課程的文化。我們的（工程教育）團隊專注於爲許多受衆提供計算機科學教育，包括谷歌工程師和世界各地的學生。在更底層的層面上，我們的（）計劃讓報名參加，以舉辦或參加同伴的講座和課程。該計劃非常成功，有數千名參與，教授的主題從技術（如瞭解現代的矢量化）到只是爲了好玩（如初級搖擺舞）。

’

’’

技術講座通常由演講者直接向聽衆介紹。另一方面，課堂可以有講座的部分，但往往以課堂練習爲中心，因此需要與會者更積極地參與。因此，與技術講座相比，教師授課的課程在創建和維護方面通常要求更高、成本也更高，而且只保留給最重要或最難的主題。也就是說，在一個課程創建之後，它的規模可以相對容易地擴大，因爲許多教員可以用同樣的課程材料來教課。我們發現，當存在以下情況時，課程往往效果最好：

主題足夠複雜，以至於經常出現誤解。課程的創建需要大量的工作，因此只有在滿足特定需求時才能開發。該主題相對穩定。更新課堂材料是一項繁重的工作，所以如果該主題快速發展，其他形式的知識共享將有更好的回報。該主題得益於有教師回答問題和提供個性化的幫助。如果學生可以在沒有指導幫助的情況下輕鬆學習，那麼像文檔或錄音這樣的自我服務媒介就會更有效率。谷歌的一些介紹性課程也有自學版本。有足夠的需求定期提供課程。否則，潛在的學習者會通過其他方式獲得他們需要的信息，而不是等待課程。在谷歌，這對於地理位置偏遠的小型辦公室來說尤其是一個問題。

>>>和，僅舉幾例。>>>>程序詳見。來自谷歌內部的洞察力，將改變你的生活和領導方式（紐約：十二書局，年）。該書包括對該計劃不同方面的描述，以及如何評估影響，並就設立類似計劃時應關注的內容提出建議。

文檔

’

文檔是書面知識，其主要目的是幫助讀者學習一些東西。並非所有的書面知識都一定是文檔，儘管它可以用作書面記錄。例如，有可能在一個郵件列表線索中找到一個問題的答案，但線索上的原始問題的主要目標是尋求答案，其次纔是爲其他人記錄討論情況。

在這一節中，我們着重於發現爲正式文件做出貢獻的機會，小到修正一個錯別字，大到記錄內部知識等。

更新文檔

’“”

你第一次學習某樣東西的時候，最好是看看如何改進現有的文檔和培訓材料。當你吸收並理解了一個新的流程或系統時，你可能已經忘記了入門文檔中的難點或缺少哪些簡單的步驟文檔。在這個階段，如果你發現文件中的錯誤或遺漏，就把它改正過來離開營地時要比你發現時更乾淨，並嘗試自己更新文件，即使文檔屬於組織的其他部門。

在谷歌，工程師們覺得無論文檔的所有者是誰，都有權更新文檔我們經常這樣做即使修復的範圍很小，比如糾正一個拼寫錯誤。這種社區維護的水平隨着的引入而明顯提高，這使得更容易找到一個文檔的所有者來審查他們的建議。這也讓可審覈的變更歷史記錄與代碼的變更歷史記錄相同。

創建文檔

隨着你的熟練程度的提高，編寫你自己的文檔並更新現有的文檔。例如，如果你建立了一個新的開發流程，就把這些步驟記錄下來。然後，你可以讓別人更容易沿着你的道路走下去，把他們引導到你的文檔。甚至更好的是，讓人們自己更容易找到這個文件。任何足以讓人無法發現或無法搜索的文件都可能不存在。這是大放異彩的另一個領域，因爲文檔可預測地位於源代碼旁邊，而不是在某個（無法找到的）文檔或網頁上。

’’

最後，確保有一個反饋的機制。如果沒有簡單直接的方法讓讀者指出文檔過時或不準確，他們很可能懶得告訴別人，而下一個新來的人也會遇到同樣的問題。如果人們覺得有人會真正注意到並考慮他們的建議，他們就會更願意做出改變。在谷歌，你可以直接從文檔本身提交一個文檔錯誤。

’

此外，可以輕鬆地在頁面上留下評論。其他可以看到並回復這些評論，而且，由於留下評論會自動爲文檔擁有者歸檔一個錯誤，讀者不需要弄清楚該與誰聯繫。

推廣文檔

“”

傳統上，鼓勵工程師記錄他們的工作可能是困難的。編寫文檔需要消耗編碼的時間和精力，而且這些工作所帶來的好處並不直接，大部分是由其他人獲益的。鑑於許多人可以從少數人的時間中獲益，像這樣的不對稱權衡對整個組織來說是好的，但如果沒有好的激勵措施，鼓勵這樣的行爲是很有挑戰性的。我們在第頁的激勵和認可一節中討論了其中的一些結構性激勵。

然而，文檔作者往往可以直接從編寫文檔中受益。假設團隊成員總是向你尋求幫助，以調試某些種類的生產故障。記錄你的程序需要前期的時間投入，但在這項工作完成後，你可以在未來節省時間，指點團隊成員去看文檔，只在需要時親自提供幫助。

’

編寫文檔也有助於你的團隊和組織的擴展。首先，文檔中的信息成爲規範化的參考：團隊成員可以參考共享的文檔，甚至自己更新它。其次，規範化可能擴散到團隊之外。也許文檔中的某些部分對團隊的配置來說並不獨特，對其他想要解決類似問題的團隊來說變得有用。

>“”’>>見童子軍規則和，《每個程序員應該知道的件事》（波士頓：，）。>>“”’>是文檔的縮寫。是谷歌單倉庫源碼庫的當前化身的名稱。

代碼

在元層面上，代碼就是知識，所以寫代碼的行爲本身可以被認爲是一種知識的轉錄。雖然知識共享可能不是生產代碼的直接目的，但它往往是一個副產品，它可以通過代碼的可讀性和清晰性來促進。

’

代碼文檔是分享知識的一種方式；清晰的文檔不僅有利於庫的使用者，而且也有利於後繼的維護者。同樣地，實現註釋也能跨時空傳播知識：你寫這些註釋是爲了未來的讀者（包括未來的你！）。就權衡利弊而言，代碼註釋和一般的文檔一樣有缺點：它們需要積極維護，否則很快就會過時，任何讀過與代碼直接矛盾的註釋的人都可以證明這一點。

’

代碼審查（見第章）對作者和審查者來說都是一個學習機會。例如，審查者的建議可能會給作者帶來新的測試模式，或者審查者可能通過看到作者在他們的代碼中使用一個新的庫來了解它。谷歌通過代碼審查的可讀性過程來規範指導，在本章末尾的案例研究中詳細介紹了這一點。

’擴展組織的知識

隨着組織的發展，確保專業知識在整個組織內得到適當的分享變得更加困難。有些事情，比如文化，在每一個成長階段都很重要，而其他事情，比如建立規範的信息源，可能對更成熟的組織更有利。

培養知識共享文化

組織文化是許多公司視爲事後諸葛亮的東西。但在谷歌，我們相信首先關注文化和環境會比只關注該環境的產出（如代碼）帶來更好的結果。

’

進行重大的組織轉變是很難的，關於這個主題的書已經不計其數。我們並不假設擁有所有的答案，但我們可以分享谷歌爲創造一種促進學習的文化而採取的具體步驟。

’

請參閱《工作規則》一書，對谷歌的文化進行更深入的研究。

>>>來自谷歌內部的洞察力，將改變你的生活和領導方式（紐約：十二書局，）。>>>>同上。

尊重

’

僅僅幾個人的不良行爲就可以使整個團隊或社區不受歡迎。在這樣的環境中，新手將會把問題轉移到其他地方，而潛在的新專家則停止嘗試，沒有成長的空間。在最糟糕的情況下，這個團體會只剩下有有毒的成員。要從這種狀態中恢復過來很困難。

“”’’’

知識分享可以而且應該以善意和尊重的方式進行。在科技界，對聰明的混蛋的容忍還有更糟糕的是，崇尚聰明的混蛋，即是普遍又是危害的，但作爲一個專家和善良並不互斥。谷歌軟件工程職位階梯的領導力部分清楚地概述了這一點：雖然在更高的層次上需要衡量技術領導力，但並非所有的領導力都針對技術問題。領導者可以提高周圍人的素質，改善團隊的心理安全感，創造團隊合作文化，化解團隊內部的緊張情緒，樹立谷歌文化和價值觀的榜樣，讓谷歌成爲一個更具活力和激情的工作場所。混蛋不是好領導。

“”

這種期望是由高級領導層示範的（技術基礎設施高級副總裁）和（副總裁，谷歌的創始人）寫了一份經常被引用的內部文件（），說明爲什麼谷歌人應該關心工作中的尊重行爲以及如何做。

獎勵和認可

’’

良好的文化必須積極培育，而鼓勵知識共享的文化需要獲得在系統層面上認可和獎勵。一個常見的錯誤是，組織在口頭上支持一套價值觀的同時，積極獎勵那些不執行這些價值觀的行爲。人們對語言的表揚很難有感覺，因此，通過建立薪酬和獎勵制度，把錢放在嘴邊就很重要的。

谷歌使用了各種認可機制，從全公司的標準，如績效審查和晉升標準到谷歌員工同行獎勵。

我們的軟件工程師級別用於校準整個公司的薪酬和晉升等獎勵，通過明確記錄這些期望，鼓勵工程師分享知識。在更高的層次上，級別明確指出了更廣泛影響力的重要性，這種期望隨着資歷的增加而增加。在最高級別，領導力的例子包括以下內容：

通過擔任初級員工的導師，幫助他們在技術和谷歌角色上發展，培養未來的領導者。通過代碼和設計審查、工程教育和開發以及對該領域其他人的專家指導，維持和發展谷歌的軟件社區。

工作階梯的期望是一種自上而下引導文化的方式，但文化也是自下而上形成的。在谷歌，同行獎金計劃是我們擁抱自下而上文化的一種方式。同行獎金是一種貨幣獎勵和正式認可，任何谷歌員工都可以將其授予任何其他谷歌員工，以表彰他們的超越性工作。例如，當將同行獎金髮給，因爲她是一個郵件列表的頂級貢獻者定期回答問題，使許多讀者受益，他公開承認她的知識共享工作及其對團隊以外的影響。由於同行獎金是由員工驅動的，而不是由管理層驅動的，因此它們可以產生重要而強大的基層效應。

與同行獎金相似的是嘉獎：對貢獻的公開承認（通常比那些值得同行獎金的影響或努力要小），提高同行貢獻的知名度。

’’’’

當一個給另一個頒發同行獎金或嘉獎時，他們可以選擇在獎勵郵件上抄送其他組或個人，提高對同行工作的認可。收件人的經理將獎勵郵件轉發給團隊以慶祝彼此的成就也很常見。

’’

一個人們可以正式和容易地認可他們的同行系統是一個強大的工具，可以鼓勵同行繼續做他們所做的了不起的事情。重要的不是獎金：而是同行的認可。

>’>>同行獎金包括現金獎勵和證書，以及在一個名爲的內部工具中成爲獎勵記錄的永久組成部分。

建立規範的信息源

規範的信息源是集中的、公司範圍的信息庫，提供了一種標準化和傳播專家知識的方法。它們最適用於與組織內所有工程師相關的信息，否則容易出現信息孤島。例如，建立一個基本的開發者工作流程的指南應該成爲規範，而運行一個本地實例的指南則只與從事的工程師有關。

建立規範的信息源需要比主要獲取更本地化的信息（如團隊文檔）更高的投資，但也有更多的好處。爲整個組織提供集中的參考資料，使廣泛需要的信息更容易找到，也更可預測，並解決了信息碎片化的問題，因爲這些問題可能會在多個處理類似問題的團隊制定自己的指南時出現，這些指南往往相互衝突。

’

因爲規範信息是高度可見的，並且旨在提供組織層面的共同理解，所以內容由主題專家積極維護和審覈是很重要的。主題越複雜，規範內容的所有者就越明確。善意的讀者可能會看到某些東西已經過時，但缺乏進行修復所需的重大結構更改的專業知識，即使工具可以很容易地提出更新建議。

創建和維護集中的、規範的信息來源是昂貴和耗時的，而且不是所有的內容都需要在組織層面上共享。當考慮在這個資源上投入多少精力時，要考慮你的受衆。誰會從這些信息中受益？你嗎？你的團隊？你的產品領域？所有的工程師？

開發者指南

谷歌爲工程師提供了一套廣泛而深入的官方指導，包括風格指南、官方軟件工程最佳實踐、代碼審查和測試指南以及每週提示（）。

’

信息庫是如此之大，以至於期望工程師從頭到尾讀完它是不切實際的，更不用說能夠一次吸收這麼多信息了。相反，已經熟悉某項準則的專家可以將鏈接發送給工程師同事，他們可以閱讀參考資料並瞭解更多信息。專家不需要親自解釋公司範圍內的做法，從而節省了時間，而學習者現在知道有一個值得信賴的信息的典型來源，他們可以在需要時訪問。這樣過程可以擴展知識，因爲它使專家能夠通過利用共同的、可擴展的資源來重新認識和解決特定的信息需求。

>>>如谷歌公司有關軟件工程的書籍。>>>>見第章。>>>>見第章。>>>>可用於多種語言。對外可用於，在。

鏈接

’“”“”’

’“”’

（有時被稱爲鏈接）是谷歌的內部縮短器。大多數谷歌內部的參考資料至少有一個內部。例如，提供關於的信息，是谷歌的開發者指南。這些內容可以存在於任何資源庫中（、、等），但有一個指向它的提供了一種可預測的、可記憶的訪問方式。這產生了一些很好的好處：

非常短，很容易在談話中分享它們（你應該看看！）。這比去找一個鏈接，然後給所有感興趣的人發一個消息要容易得多。有一個低成本的方式來分享參考資料，使得這些知識更有可能在第一時間被分享。提供內容的固定鏈接，即使底層的發生變化。當所有者將內容移到一個不同的資源庫時（例如，將內容從移到），他們可以簡單地更新的目標。本身保持不變。

’

在谷歌文化中根深蒂固，以至於出現了一個良性循環：一個尋找信息的可能會首先查看。如果沒有指向開發者指南（如預期），一般會自己配置鏈接。因此，通常可以在第一次嘗試時猜出正確的。

代碼實驗室

’

是有指導的實踐教程，通過結合解釋、工作中的最佳實踐示例代碼和代碼練習，向工程師傳授新概念或流程。上提供了一個規範的集合，用於廣泛使用的技術。這些代碼集在發佈前經過了幾輪正式的審查和測試。是介於靜態文檔和講師指導課程之間的一個有趣的中間點，它們分享了兩者的最佳和最差的特點。它們的實踐性使它們比傳統的文檔更有吸引力，但工程師仍然可以按需訪問它們，並自行完成；但它們的維護成本很高，而且不適合學習者的特定需求。

>>>與語言無關。>>>>外部代碼實驗室可在。

靜態分析

靜態分析工具是分享編程檢查最佳實踐的強大方式。每種編程語言都有其特定的靜態分析工具，它們有相同的共同目的：提醒代碼作者和審查者注意可以改進代碼的方式，以遵循規範和最佳實踐。有些工具更進一步，提供自動將這些改進應用到代碼中。

’

設置靜態分析工具需要前期投入，但一旦這些工具到位，它們就會有效地擴展。當最佳實踐的檢查被添加到一個工具中時，每個使用該工具的工程師都會意識到這是最佳實踐。這也使工程師們可以騰出時間來教其他東西：原本用於手動教授（現在是自動的）最佳實踐的時間和精力，可以用來教授其他東西。靜態分析工具增強了工程師的知識。它們使一個組織能夠應用更多的最佳實踐，並比其他方式更一致地應用它們。

保持互動

’

有些信息對於完成工作至關重要，例如知道如何執行典型的開發工作流。其他的信息，比如流行的生產力工具的更新，雖然不那麼關鍵，但仍然有用。對於這種類型的知識，信息共享媒介的正式性取決於所傳遞信息的重要性。例如，用戶希望官方文檔保持最新，但通常對新聞稿內容沒有這樣的期待，因此新聞稿內容需要所有者進行較少的維護和保養。

時事通訊

’’’

谷歌有一些發給所有工程師的公司範圍內的新聞簡報，包括（工程新聞），（隱私安全新聞），以及谷歌的（本季度最有趣的故障報告）。這些都是傳達工程師感興趣但並非關鍵任務的信息的好方法。對於這種類型的更新，我們發現，如果通訊發送的頻率較低，並且包含更多有用的、有趣的內容，就會得到更好的參與度。否則，新聞簡報會被認爲是垃圾郵件。

儘管大多數谷歌新聞通訊都是通過電子郵件發送的，但有些新聞通訊的發送方式更有創意。廁所測試（測試提示）和廁所學習（產品活動提示）是張貼在廁所裏的單頁新聞通訊。這種獨特的發送媒介幫助廁所測試和廁所學習從其他新聞通訊中脫穎而出，而且所有期刊都在在線存檔。

社區

谷歌人喜歡圍繞各種主題建立跨組織的社區和分享知識。這些開放的渠道可以讓你更容易地向周圍的人學習，避免信息孤島和重複。谷歌羣組尤其受歡迎：谷歌有數千個內部團體，形式各異。有些專門用於故障排除；其他人，如代碼健康小組，更多的是討論和指導。內部作爲非正式信息來源在谷歌用戶中也很受歡迎，因爲人們會發布有趣的技術分類或他們正在從事的項目的詳細信息。

可讀性：通過代碼審查實現標準化指導

“”

在谷歌，可讀性指的不僅僅是代碼的可讀性；這是一個標準化的、谷歌範圍內的指導過程，用於傳播編程語言最佳實踐。可讀性涵蓋了廣泛的專業知識，包括但不限於語言語義、代碼結構、設計、通用庫的正確使用、文檔和測試覆蓋率。

’“”’’

可讀性最初是一個人的努力。在谷歌早期，（員工）會親自與每一位新員工坐下來，逐行對他們的第一個主要代碼提交進行“可讀性審查”。這是一次挑剔的審查，涵蓋了從代碼改進到空白約定的所有方面。這讓谷歌的代碼庫有了統一的模式，但更重要的是，它教授了最佳實踐，強調了什麼是可用的共享基礎設施，並向新員工展示了在谷歌編寫代碼的感覺。

’

不可避免地，谷歌的招聘速度越來越快，超出了一個人的能力範圍。如此多的工程師發現這個過程很有價值，於是他們自願拿出自己的時間來擴展這個項目。今天，大約有的谷歌工程師在任何時候都在參與可讀性進程，他們要麼是審查員，要麼是代碼作者。

什麼是可讀性過程？

在谷歌，代碼審查是強制性的。每個變更列表（）都需要可讀性批准，這表明擁有該語言的可讀性認證的人已經批准了該。經過認證的作者隱含地對他們自己的提供可讀性批准；否則，一個或多個合格的審查員必須明確地對提供可讀性批准。這項要求是在谷歌發展到無法強制要求每個工程師接受代碼審查，從而將最佳實踐傳授到所需的嚴格程度之後添加的。

“”’’

在谷歌內部，擁有可讀性認證通常被稱爲一門語言的可讀性。擁有可讀性認證的工程師已經證明，他們始終如一地寫出清晰、習慣和可維護的代碼，體現了谷歌對特定語言的最佳實踐和編碼風格。他們通過可讀性程序提交，在此過程中，一個集中的可讀性審查員小組審查，並就它在多大程度上展示了各個領域的掌握程度給出反饋。隨着作者對可讀性準則的內化，他們收到的關於他們的的評論越來越少，直到他們最終從這個過程中畢業並正式獲得可讀性。可讀性帶來了更多的責任：擁有可讀性的工程師被信任，可以繼續將他們的知識應用於他們自己的代碼，並作爲其他工程師的代碼的審查者。

“’”“”

大約有到的谷歌工程師是可讀性審查員。所有的審查員都是志願者，任何有可讀性的人都歡迎自我提名成爲可讀性審查員。可讀性審查員被要求達到最高標準，因爲他們不僅要有深厚的語言專業知識，還要有通過代碼審查進行教學的能力。他們被期望把可讀性首先作爲一個指導和合作的過程，而不是一個把關或對抗的過程。我們鼓勵可讀性審查員和作者在審查過程中進行討論。審查人爲他們的評論提供相關的引文，這樣作者就可以瞭解制定文體指南的理由（切斯特森的籬笆）。如果任何特定準則的理由不清楚，作者應該要求澄清（提問）。

>>>變更列表是構成版本控制系統中的一個變更的文件列表。變更列表與變更集是同義的。

可讀性是一個人爲驅動的過程，旨在以標準化但個性化的方式擴展知識。作爲書面知識和內部知識的互補混合體，可讀性結合了書面文件的優勢，可以通過可引用的參考文獻來獲取，也結合了專家審查員的優勢，他們知道應該引用哪些指南。典範指南和語言建議被全面地記錄下來這很好！但信息的語料庫非常大，可能會讓人不知所措，特別是對新人來說。

>>>截至，谷歌風格指南只有頁長。構成完整的最佳實踐語法庫的次要材料要長很多倍。

爲什麼有這個過程？

’

代碼的閱讀量遠遠大於編寫量，這種影響在谷歌的規模和我們（非常大的）中被放大。任何工程師都可以查看並學習其他團隊的代碼的豐富知識，而像這樣強大的工具使得在整個代碼庫中尋找參考資料變得很容易（見第章）。文檔化最佳實踐的一個重要特徵（見第章）是，它們爲所有谷歌代碼提供了一致的標準。可讀性是這些標準的可強制執行和傳播的基礎。

’

可讀性項目的主要優勢之一是，它讓工程師接觸到的不僅僅是他們自己團隊的內部知識。爲了獲得特定語言的可讀性，工程師們必須將發送給一組集中的可讀性審查員，他們審查整個公司的代碼。將流程集中化會帶來顯著的折衷：該計劃僅限於隨着組織的發展而線性擴展，而不是亞線性擴展，但它更容易實現一致性，避免孤島，並避免（通常是無意的）偏離既定規範。

’

整個代碼庫的一致性的價值怎麼強調都不爲過：即使數十年來有數萬名工程師編寫代碼，它也確保了一門語言中的代碼在整個語法庫中看起來都是相似的。這使讀者能夠專注於代碼的作用，而不是被爲什麼它看起來與他們習慣的代碼不同而分散注意力。大規模的變更作者（見第章）可以更容易地在整個語法庫中進行變更，跨越成千上萬個團隊的界限。人們可以更換團隊，並確信新的團隊使用特定語言的方式不會與他們以前的團隊有很大的不同。

>’>>有關谷歌使用的原因，請參閱還要注意的是，並非谷歌的所有代碼都存在於中；此處描述的可讀性僅適用於，因爲它是存儲庫內一致性的概念。

這些好處伴隨着一些成本：與文檔和類等其他媒介相比，可讀性是一個重量級的過程，因爲它是強制性的，並由谷歌工具化強制執行（見第章）。這些成本是不小的，包括以下幾點：

對於那些沒有任何團隊成員具備可讀性的團隊來說，增加了衝突，因爲他們需要從團隊之外尋找審查員來對進行可讀性審批。對於需要可讀性審查的作者來說，有可能需要額外的幾輪代碼審查。作爲一個由人驅動的過程，其擴展性成爲瓶頸。由於它依賴於人類審查員進行專門的代碼審查，所以對組織的增長具有線性擴展的限制。

’

那麼，問題是收益是否大於成本。還有一個時間因素：收益與成本的全部效果並不在同一時間維度上。該計劃對增加的短期代碼審查延遲和前期成本進行了慎重的權衡，以獲得更高質量代碼、存儲庫範圍內的代碼一致性和增加的工程師專業知識的長期回報。效益的時間尺度較長，期望編寫的代碼有幾年甚至幾十年的潛在壽命。

’

與大多數或許是所有的工程過程一樣，總是有改進的餘地。一些成本可以通過工具來降低。許多可讀性註釋解決了靜態檢測和靜態分析工具自動註釋的問題。隨着我們對靜態分析的不斷投資，可讀性審查員可以越來越多地關注更高層次的領域，比如某個特定的代碼塊是否可以被不熟悉代碼庫的外部讀者所理解，而外部讀者不熟悉代碼庫，而不是自動檢測，例如行是否有尾隨空白。

’’’

但光有願望是不夠的。可讀性是一個有爭議的項目：一些工程師抱怨說這是一個不必要的官僚主義，是對工程師時間的浪費。可讀性的權衡是值得的嗎？爲了找到答案，我們求助於我們可信賴的工程生產力研究（）團隊。

團隊對可讀性進行了深入的研究，包括但不限於人們是否受到這個過程的阻礙，是否學到了什麼，或者畢業後是否改變了他們的行爲。這些研究表明，可讀性對工程速度有正向的積極影響。具有可讀性的作者的比不具有可讀性的作者的在統計上要少花時間。具有可讀性的工程師與不具有可讀性的工程師相比，自我報告的對其代碼質量的滿意度缺乏對代碼質量更客觀的衡量標準更高。絕大多數完成該計劃的工程師對這一過程表示滿意，並認爲這是值得的。他們報告說從審查員那裏學到了東西，並改變了自己的行爲，以避免在編寫和評審代碼時出現可讀性問題。

’’

谷歌有着非常濃厚的代碼審查文化，可讀性是這種文化的延伸。可讀性從一個工程師的熱情發展到一個由專家組指導所有谷歌工程師的正式項目。它隨着谷歌的成長而不斷發展變化，並將隨着谷歌需求的變化而繼續發展。

>’>>因此，已知時間跨度較短的代碼不受可讀性要求的約束。考試示例包括實驗目錄（明確指定爲實驗代碼，不能推動生產）和計劃，這是谷歌實驗產品的研討會。>>>>這包括控制各種因素，包括在谷歌的任職期限，以及與已經具備可讀性的作者相比，沒有可讀性的作者的通常需要額外的審查。

結論

在某些方面，知識是軟件工程組織最重要的（儘管是無形的）資產，而知識的共享對於使組織在面對變化時具有彈性和冗餘至關重要。一種促進開放和誠實的知識共享的文化可以在整個組織內有效地分配這些知識，並使該組織能夠隨着時間的推移而擴展。在大多數情況下，對更容易的知識共享的投入會在一個公司的生命週期中獲得許多倍的回報。

內容提要

心理安全是培養知識共享環境的基礎。從小事做起：問問題，把事情寫下來。讓人們可以很容易地從專家和有記錄的參考資料中獲得他們需要的幫助。在系統的層面上，鼓勵和獎勵那些花時間去教授和擴大他們的專業知識，而不僅僅是他們自己、他們的團隊或他們的組織。沒有什麼靈丹妙藥：增強知識共享文化需要多種策略的結合，而最適合你的組織的確切組合可能會隨着時間的推移而改變。