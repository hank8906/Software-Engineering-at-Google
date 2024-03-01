第七章度量工程效率

谷歌是一家數據驅動型公司。我們的大部分產品和設計決策都有可靠的數據支持。數據驅動的決策文化，使用適當的指標，有一些不足，但總的來說，依靠數據往往使大多數決策變得客觀而不是主觀，這往往是一件好事。然而，收集和分析數據是人性的弱點，有其自身的挑戰。具體來說，在軟件工程領域，谷歌發現，隨着公司規模的擴大，擁有一支專注於工程生產效率的專家團隊本身是非常有價值和重要的，可以利用這樣一支團隊的洞察力。

我們爲什麼要度量工程效率

’’’’

讓我們假設你有一個蓬勃發展的業務（例如，你經營一個在線搜索引擎），並且你想擴大你的業務範圍（進入企業應用市場，或雲市場，或移動市場）。據推測，爲了增加你的業務範圍，你也需要增加你的工程組織的規模。然而，隨着組織規模的線性增長，溝通成本也呈二次曲線增長。增加人員對擴大業務範圍是必要的，但溝通成本不會隨着你增加人員而線性擴展。因此，你將無法根據你的工程組織的規模線性地擴大你的業務範圍。

不過，還有一種方法可以解決我們的規模問題：我們可以使每個人的生產效率提高。如果我們能提高組織中單個工程師的生產效率，我們就能增加我們的業務範圍，而不會相應地增加溝通成本。

谷歌不得不迅速發展新業務，這意味着要學習如何讓我們的工程師更有效率。要做到這一點，我們需要了解是什麼讓他們富有成效，找出我們工程流程中的低效之處，並解決所發現的問題。然後，我們將根據需要在一個持續改進的循環中重複這個循環。通過這樣做，我們將能夠在需求增加的情況下擴展我們的工程組織。

然而，這個增量改進過程同樣需要人力資源。如果每年需要個工程師來了解和解決生產力的障礙，那麼以每年名工程師的數量來提高工程組織的生產率是不值當的。因此，我們不僅要在目標上提高軟件工程的生產力，而且這一改進過程也要同樣高效。

在谷歌，我們通過建立一個致力於瞭解工程生產效率的研究團隊來解決這些權衡問題。我們的研究團隊包括來自軟件工程研究人員和普通的軟件工程師，但我們也包括來自不同領域的社會學家，包括認知心理學和行爲經濟學。來自社會科學的人員的加入使我們不僅可以研究工程師生產的軟件構件，還可以瞭解軟件開發過程中人的一面，包括個人動機、激勵結構和管理複雜任務的策略。該團隊的目標是採用數據驅動的方法來度量和提高工程生產效率。

在本章中，我們將介紹我們的研究團隊是如何實現這一目標的。這從分類過程開始：我們對軟件開發的許多部分可以進行計量，但是我們到底應該計量什麼呢？在一個項目被選中後，我們將介紹研究團隊如何確定有意義的指標，以確定該過程中存在問題的部分。最後，我們看一下谷歌是如何使用這些指標來跟蹤生產效率的改進。

’

在本章中，我們遵循谷歌的和語言團隊提出的一個具體例子：可讀性。在谷歌存在的大部分時間裏，這些團隊一直在管理谷歌的可讀性過程。關於可讀性的更多信息，請參見第三章）。可讀性過程是在谷歌的早期建立的，當時自動格式化工具（第章）和阻止提交的鎖定還沒有普及（第章）。這個過程本身運行成本很高，因爲它需要數以百計的工程師爲其他工程師進行可讀性審查，以便授予他們可讀性。一些工程師認爲這是一個古老的自欺欺人過程，不再具有實用性，這也是午餐桌上最喜歡爭論的話題。來自語言團隊的具體問題是：花在可讀性過程上的時間是值得的嗎？

>>>，《人月神話：軟件工程隨筆》（紐約：，）。

分類：是否值得度量？

’’’

在我們決定如何度量工程師的生產效率之前，我們需要知道某個指標是否值得度量。度量本身是昂貴的：它需要人去度量過程，分析結果，並將其傳播給公司的其他部門。此外，度量過程本身可能是繁瑣的，會拖累工程組織的其他部門。即使它不慢，跟蹤進度也可能改變工程師的行爲，可能會掩蓋潛在的問題。我們需要聰明地度量和估計；雖然我們不想猜測，但我們不應該浪費時間和資源進行不必要的度量。

’’

在谷歌，我們想出了一系列的問題來幫助團隊確定是否值得優先度量生產效率。我們首先要求人們以具體問題的形式描述他們想要度量的東西；我們發現，人們提出這個問題越具體，他們就越有可能從這個過程中獲益。當可讀性團隊與我們接觸時，其問題很簡單：工程師在提高可讀性過程中的成本增加是否匹配他們爲公司帶來的好處？

“”’

’’’“”

然後我們要求他們考慮以下問題：

你期望的結果是什麼？爲什麼？儘管我們可能想假裝我們是中立的調查人員，但事實並非如此。我們確實對一些事有先入爲主的觀念。通過一開始就承認這一點，我們可以嘗試解決這些偏見，防止對結果進行事後解釋。當這個問題被提給可讀性小組時，該小組指出，它並不確定。人們確信在某個時間點上，成本是值得的，但是隨着自動格式化和靜態分析工具的出現，沒有人完全確定。越來越多的人認爲，這個過程現在成了一種自欺欺人的儀式。雖然它可能仍然爲工程師提供了好處（他們有調查數據顯示人們確實聲稱有這些好處），但不清楚它是否值得作者或代碼審查員投入時間。

如果數據支持你的預期結果，將採取什麼行動我們這樣問是因爲如果不採取任何行動，那麼度量就沒有意義了。請注意，如果沒有這一結果，就會發生計劃變更，那麼行動實際上可能是“維持現狀”。當被問及這個問題時，可讀性團隊的回答很直截了當：如果好處足以證明這個過程的成本是合理的，他們會鏈接到關於可讀性的上的研究和數據，並進行宣傳以設定期望。

如果我們得到一個負面的結果，是否會採取適當的行動？我們問這個問題是因爲在許多情況下，我們發現負面結果不會改變決策。決策中可能會有其他的投入，而這些投入將取代任何負面的結果。如果是這樣的話，可能一開始就不值得度量。這也是阻止我們研究團隊所做的大多數項目的問題；我們瞭解到決策者對了解結果感興趣，但由於其他原因，他們不會選擇改變方向。然而，在可讀性的案例中，我們有一個來自團隊的強有力的行動聲明。它承諾，如果我們的分析顯示成本大於收益，或者收益可以忽略不計，團隊將放棄這個項目。由於不同的編程語言在格式化和靜態分析方面有不同的成熟度，因此該評估將基於每種語言進行。

誰將決定對結果採取行動，以及他們何時採取行動？我們這樣問是爲了確保要求度量的人是被授權採取行動的人（或直接代表他們採取行動）。歸根結底，度量我們的軟件流程的目的是幫助人們做出業務決策。瞭解這個人是誰很重要，包括什麼形式的數據能說服他們。儘管最好的研究包括各種方法（從結構化訪談到日誌的統計分析等各種方法），但爲決策者提供他們需要的數據的時間可能有限。在這些情況下，最好的辦法是迎合決策者的要求。他們是否傾向於通過訪談中可以獲取到的故事來做出決策？他們是否信任調查結果或日誌數據？他們對複雜的統計分析感到滿意嗎？如果決策者壓根就不相信結果的形式，那麼度量過程又沒有意義。在可讀性方面，我們對每種編程語言都有一個明確的決策者。有兩個語言團隊，即和，積極向我們尋求幫助，而其他團隊則在等待，看這些語言先發生什麼。決策者相信工程師自我報告的經驗，以瞭解快樂和學習，但決策者希望看到基於日誌數據的速度和代碼質量的硬數字。這意味着，我們需要對這些指標進行定性和定量分析。這項工作沒有一個硬性的截止日期，但有一個內部會議，如果有變化的話，這個會議將宣佈一個新的時間點。這個期限給了我們幾個月的時間來完成這項工作。

’’

’’’

’

’’’

’

通過問這些問題，我們發現在許多情況下，度量根本不值得這沒有關係！有許多很好的理由不度量一個工具或過程對生產效率的影響。以下是我們看到的一些例子：

至少在現階段，你承擔不了改變這個過程工具的成本可能有時間上的限制或資金上的制約，使之無法進行。例如，你可能確定，只要你切換到一個更快的構建工具，每週就能節省幾個小時的時間。然而，轉換意味着在每個人都轉換的時候暫停開發，而且有一個重要的資金期限即將到來，這樣你就無法承受這種中斷。工程權衡不是在真空中評估的在這樣的情況下，重要的是要意識到，更廣泛的背景完全可以說明推遲對結果採取行動是合理的。

任何結果很快就會因其他因素而失效這裏的例子可能包括在計劃重組之前度量一個組織的軟件流程。或者度量一個被廢棄的系統的技術債務的數量。決策者有強烈的意見，而你不太可能提供足夠多的正確類型的證據，來改變他們的信念。這就需要了解你的受衆。即使在谷歌，我們有時也會發現一些人由於他們過去的經驗而對某一主題有堅定的信念。我們曾發現一些利益相關者從不相信調查數據，因爲他們不相信自我觀念。我們也發現一些利益相關者，他們最容易被由少量訪談得出的令人信服的敘述所動搖。當然，也有一些利益相關者只被日誌分析所動搖。在所有情況下，我們都試圖用混合方法對真相進行三角分析，但如果利益相關者只限於相信不適合問題的方法，那麼做這項工作就沒有意義。

結果只能作爲浮華的指標，以來支持你一定要做的事情這也許是我們在谷歌告訴人們不要度量軟件過程的最常見的原因。很多時候，人們已經爲多個原因規劃了一個決策，而改進軟件開發過程只是這些決策的一個好處。例如，谷歌的發佈工具團隊曾經要求對發佈工作流程系統的計劃變更進行度量。由於變化的性質，很明顯，這個變化不會比目前的狀態差，但他們不知道這是一個小的改進還是一個大的改進。我們問團隊：如果結果只是一個小的改進，無論如何你會花資源來實現這個功能，即使它看起來不值得投資？答案是肯定的這個功能碰巧提高了生產效率，但這是一個副作用：它也更具有性能，降低了發佈工具團隊的維護負擔。

唯一可用的指標不夠精確，無法度量問題，而且會被其他因素所幹擾在某些情況下，所需的指標（見即將到來的關於如何識別指標的章節）根本無法獲得。在這些情況下，使用其他不那麼精確的指標（例如，編寫的代碼行）進行度量是很誘人的。然而，這些指標的任何結果都是無法解釋的。如果這個指標證實了利益相關者預先存在的觀念，他們最終可能會繼續執行他們的計劃，而不考慮這個指標不是一個準確的度量標準。如果它沒有證實他們的觀念，那麼指標本身的不精確性就提供了一個簡單的解釋，利益相關者可能再次繼續他們的計劃。

’’

當你成功地度量你的軟件過程時，你並不是爲了證明一個假設的正確與否；成功意味着給利益相關者提供他們做出決定所需的數據。如果這個利益相關者不使用這些數據，那麼這個項目就是失敗的。我們只應該在根據結果做出具體決定的時候纔去度量一個軟件過程。對於可讀性團隊來說，有一個明確的決定要做。如果度量標準顯示這個過程是有益的，他們將公佈這個結果。如果沒有，這個過程就會被廢除。最重要的是，可讀性小組有權力做出這個決定。

>’“”“”>>在此值得指出的是，我們的行業目前貶低軼事數據，而每個人都有一個數據驅動的目標。然而，軼事仍然存在，因爲它們是強大的。軼事可以提供原始數字無法提供的背景和敘述；它可以提供一個深刻的解釋，因爲它反映了個人的經驗，所以能引起別人的共鳴。雖然我們的研究人員不會根據軼事做出決定，但我們確實使用並鼓勵結構化訪談和案例研究等技術，以深入理解現象，併爲定量數據提供背景。>>’>>和擁有最大量的工具支持。兩者都有成熟的格式化工具和靜態分析工具，可以捕捉常見的錯誤。兩者也都有大量的內部資金。即使其他語言團隊，如，對結果感興趣，但顯然，如果我們連或都不能顯示出同樣的好處，那麼就不會有刪除可讀性的好處。

用目標和信號來選擇有意義的度量標準

’

在我們決定度量一個軟件過程之後，我們需要確定使用什麼指標。顯然，代碼行（）是不行的，但我們究竟該如何度量工程生產效率呢？

在谷歌，我們使用目標信號指標（）框架來指導指標創建。

’’

目標是一個期望的最終結果。它是根據你希望在高層次上理解的內容來表述的，不應包含對具體度量方法的引用。。信號是你如何知道你已經實現了最終結果。信號是我們想要度量的東西，但它們本身可能是不可度量的。指標是信號的代表。它是我們實際上可以度量的東西。它可能不是理想的度量，但它是我們認爲足夠接近的東西。

“”

框架在創建指標時鼓勵幾個理想的屬性。首先，通過首先創建目標，然後是信號，最後是指標，它可以防止路燈效應。這個詞來自於在路燈下找你的鑰匙這個完整的短語：如果你只看你能看到的地方，你可能沒有找對地方。對於指標來說，當我們使用我們容易獲得的、容易度量的指標時，就會出現這種情況，不管這些指標是否適合我們的需求。相反，迫使我們思考哪些指標能真正幫助我們實現目標，而不是簡單地考慮我們有哪些現成的指標。

’’’’

第二，通過鼓勵我們使用原則性的方法提出適當的指標集，從而有助於防止指標蔓延和指標偏差，從而有助於實際度量結果。考慮這樣一種情況，我們在沒有原則性方法的情況下選擇指標，然後結果不符合我們的利益相關者的期望。在這一點上，我們面臨着利益相關者建議我們使用他們認爲會產生預期結果的不同指標的風險。而且因爲我們一開始並沒有基於原則性的方法進行選擇，所以沒有理由說他們錯了！相反，鼓勵我們根據度量原始目標的能力選擇指標。利益相關者可以很容易地看到這些指標映射到他們的最初的目標，並提前同意這是度量結果的最佳指標集。

’

最後，可以告訴我們哪裏有度量覆蓋，哪裏沒有。當我們運行流程時，我們列出所有的目標，併爲每個目標創建信號。正如我們在例子中所看到的，並不是所有的信號都是可度量的，這沒關係！通過，至少我們已經確定了什麼是可度量的。通過，至少我們已經確定了哪些是不可度量的。通過識別這些缺失的指標，我們可以評估是否值得創建新的指標，甚至是否值得度量。

重要的是要保持可追溯性。對於每個指標，我們應該能夠追溯到它所要代表的信號，以及它所要度量的目標。這可以確保我們知道我們正在度量哪些指標，以及爲什麼我們要度量它們。

>“‘’‘’‘’‘’”>>“從那時起，用‘每月產生的代碼行數’來度量‘程序員生產效率’只需一小步。這是一個非常昂貴的度量單位，因爲它鼓勵編寫平淡的代碼，但今天我對這個單位的愚蠢程度不感興趣，甚至從純商業的角度來看也是如此。我今天的觀點是，如果我們希望計算代碼的行數，我們不應該將它們視爲“生產的行數”，而應該視爲“花費的行數”：當前的傳統智慧愚蠢到將這些行數記在賬本的錯誤一側。”，關於真正教給計算機科學的殘酷性，手稿。

目標

目標應該根據所需的屬性來編寫，而不需要參考任何指標。就其本身而言，這些目標是無法度量的，但一組好的目標是每個人都可以在繼續進行信號和度量指標之前達成一致的。

爲了使其發揮作用，我們首先需要確定一套正確的目標來度量。這看起來很簡單：團隊肯定知道他們工作的目標！但是，我們的研究團隊發現，在許多情況下，人們忘記了將所有可能的權衡因素包括在生產效率中。然而，我們的研究團隊發現，在許多情況下，人們忘記了將所有可能的生產力內的權衡因素包括在內，這可能導致錯誤的度量。

’

>

以可讀性爲例，我們假設團隊太專注於使可讀性過程快速和簡單，以至於忘記了關於代碼質量的目標。團隊設置了跟蹤度量，以瞭解通過審查過程需要多長時間，以及工程師對該過程的滿意程度。我們的一個隊友提出以下建議：

>我可以讓你的審查速度變得非常快：只要完全取消代碼審查。

“”

’

雖然這顯然是一個極端的例子，但團隊在度量時總是忘記了核心的權衡：他們太專注於提高速度而忘記了度量質量（或者反過來）。爲了解決這個問題，我們的研究團隊將生產效率分爲五個核心部分。這五個部分是相互權衡的，我們鼓勵團隊考慮每一個部分的目標，以確保他們不會在無意中提高一個部分而使其他部分下降。爲了幫助人們記住所有五個組成部分，我們使用了的記憶法：

代碼的質量產生的代碼的質量如何？測試用例是否足以預防迴歸？架構在減輕風險和變化方面的能力如何？

工程師的關注度工程師達到流動狀態的頻率如何？他們在多大程度上被通知分散了注意力？工具是否鼓勵工程師進行狀態切換？

知識的複雜性完成一項任務需要多大的認知負荷？正在解決的問題的內在複雜性是什麼？工程師是否需要處理不必要的複雜性？

節奏和速度工程師能多快地完成他們的任務？他們能以多快的速度把他們的版本推出去？他們在給定的時間範圍內能完成多少任務？

滿意程度工程師對他們的工具有多滿意？工具能在多大程度上滿足工程師的需求？他們對自己的工作和最終產品的滿意度如何？工程師是否感到筋疲力盡？

回到可讀性的例子，我們的研究團隊與可讀性團隊合作，確定了可讀性過程中的幾個生產力目標：

代碼的質量由於可讀性過程，工程師們寫出了更高質量的代碼；由於可讀性過程，他們寫出了更一致的代碼；由於可讀性過程，他們爲代碼的健康文化做出了貢獻。

來自工程師的關注我們沒有爲可讀性制定任何關注目標。這是可以的並非所有關於工程生產力的問題都涉及所有五個領域的權衡。

知識複雜性工程師們通過可讀性過程瞭解谷歌代碼庫和最佳編碼實踐，他們在可讀性過程中接受指導。

節奏和速度由於可讀性過程，工程師更快、更有效地完成工作任務。

滿意度工程師們看到了可讀性過程的好處，對參與該過程有積極的感受。

信號

’’

通過約定的信號，我們可以知曉某個目標已被實現。並非所有的信號都是可度量的，但這在現階段是可以接受的。信號和目標之間不是的關係。每個目標應該至少有一個信號，但它們可能有更多的信號。有些目標也可能共享一個信號。表顯示了可讀性過程度量的目標的一些信號示例。

表信號和目標

<><><><><>

目標信號由於可讀性過程，工程師們會寫出更高質量的代碼。被授予可讀性的工程師判斷他們的代碼比沒有被授予可讀性的工程師的質量更高。可讀性過程對代碼質量有積極影響。工程師們通過可讀性過程瞭解谷歌的代碼庫和最佳編碼實踐。工程師們報告了從可讀性過程中的學習情況。工程師在可讀性過程中接受指導。工程師們報告了與經驗豐富的谷歌工程師的積極互動，他們在可讀性過程中擔任審查員。工程師在可讀性過程中得到指導。<><>由於可讀性過程，工程師們更快、更有效地完成工作任務。<><>工程師們看到了可讀性過程的好處，並對參與這一過程有積極的感受。被授予可讀性的工程師判斷自己比沒有被授予可讀性的工程師更有生產效率。被授予可讀性的工程師所寫的修改比未被授予可讀性的工程師所寫的修改審查得更快。<><>工程師認爲可讀性過程是值得的。

指標

指標是我們最終確定如何計量、評判信號的標準。指標不是信號本身；它們是信號的可度量的代表。因爲它們是一個代表，所以它們可能不是一個完美的度量。出於這個原因，我們試圖對基本信號進行三角度量分析，一些信號可能有多個指標。

’

例如，爲了度量工程師的代碼在可讀性之後是否審查得更快，我們可能會同時使用調查數據和日誌數據。這兩個指標都沒有真正提供基本的事實。人類的感知是易變的，而日誌指標可能沒有度量出工程師審查一段代碼所花時間的全貌，或者可能被當時未知的因素所混淆，比如代碼修改的大小或難度。然而，如果這些指標顯示出不同的結果，就表明可能其中一個指標是不正確的，我們需要進一步探索。如果它們是一樣的，我們就更有信心，我們已經達到了某種真相。

此外，一些信號可能沒有任何相關的指標，因爲信號可能在這個時候根本無法度量。例如，考慮度量代碼質量。儘管學術文獻已經提出了許多代碼質量的代用指標，但沒有一個能真正抓住它。對於可讀性，我們必須做出決定，要麼使用一個糟糕的代表，並可能根據它做出決定，要麼乾脆承認這是一個目前無法度量的點。最終，我們決定不把它作爲一個量化的指標，儘管我們確實要求工程師對他們的代碼質量進行自我評價。

’

遵循框架是一個很好的方法，可以明確你爲什麼要度量你的軟件過程的目標，以及它將如何被實際度量。然而，仍然有可能選擇的指標沒有說明全部情況，因爲它們沒有捕獲所需的信號。在谷歌，我們使用定性數據來驗證我們的指標，並確保它們捕捉到了預期的信號。

使用數據驗證指標

’“”’’“”“”

舉個例子，我們曾經創建了一個度量每個工程師平均構建延遲中位數的指標；目的是爲了捕捉工程師構建延遲的典型經驗。然後我們進行了一個經驗抽樣研究。在這種研究方式中，工程師在做一項感興趣的任務時被打斷，以回答一些問題。在工程師開始構建後，我們自動向他們發送了一份小型調查，瞭解他們對構建延遲的經驗和期望。然而，在少數情況下，工程師們回答說他們沒有開始構建！結果發現，自動化工具正在啓動。事實證明，自動化工具正在啓動構建，但工程師們並沒有被這些結果所阻礙，因此它並沒有“計入”他們的“典型經驗”。然後我們調整了指標，排除了這種構建。

’’

定量指標是有用的，因爲它們給你能力和規模。你可以在很長一段時間內度量整個公司的工程師的經驗，並對結果有信心。然而，它們並不提供任何背景或敘述。定量指標不能解釋爲什麼一個工程師選擇使用一個過時的工具來完成他們的任務，或者爲什麼他們採取了一個不尋常的工作流程，或者爲什麼他們繞過了一個標準流程。只有定性研究才能提供這些信息，也只有定性研究才能爲改進流程的下一步提供洞察力。

>>>我們在谷歌的常規經驗是，當定量指標和定性指標不一致時，是因爲定量指標沒有捕捉到預期的結果。

現在考慮一下表中提出的信號。你可以創建什麼指標來度量其中的每一個？其中一些信號可能是可以通過分析工具和代碼日誌來度量的。其他的只能通過直接詢問工程師來度量。還有一些可能不是完全可度量的例如，我們如何真正度量代碼質量？

最終，在評估可讀性對生產力的影響時，我們最終綜合了三個方面的指標。首先，我們有一個專門針對可讀性過程的調查。這個調查是在人們完成了這個過程之後進行的；這使我們能夠得到他們對這個過程的即時反饋。這有望避免回憶偏差，但它確實引入了近期偏差和抽樣偏差。其次，我們使用大規模的季度調查來追蹤那些不是專門關於可讀性的項目；相反，它們純粹是關於我們預期可讀性應該影響的指標。最後，我們使用了來自我們的開發者工具的細粒度的日誌指標來確定日誌中聲稱的工程師完成特定任務所需的時間。表列出了完整的指標清單及其相應的信號和目標。

表目標、信號和指標

<><><>’’’

目標信號指標代碼的質量由於可讀性過程，工程師們會寫出更高質量的代碼。被授予可讀性的工程師判斷他們的代碼比沒有被授予可讀性的工程師的質量更高。<><>可讀性過程對代碼質量有積極影響。季度調查。對自己的代碼質量表示滿意的工程師的比例<><>可讀性調查。報告可讀性審查對代碼質量沒有影響或有負面影響的工程師的比例可讀性調查。報告說參與可讀性過程改善了他們團隊的代碼質量的工程師的比例作爲可讀性過程的結果，工程師們寫出的代碼更加一致。工程師在代碼審查中由可讀性審查員提供一致的反饋和指導，這是可讀性過程的一部分。可讀性調查。報告可讀性審查員的意見和可讀性標準不一致的工程師比例。工程師對代碼健康文化的貢獻是可讀性過程的結果。被授予可讀性的工程師經常在代碼審查中評論風格和或可讀性問題。可讀性調查：報告他們經常在代碼審查中評論風格和或可讀性問題的工程師的比例工程師的關注不適用不適用不適用知識工程師們通過可讀性過程瞭解谷歌的代碼庫和最佳編碼實踐。工程師們報告了從可讀性過程中的學習情況。可讀性調查。報告說他們瞭解了四個相關主題的工程師比例可讀性調查：報告學習或獲得專業知識是可讀性過程的優勢的工程師比例工程師在可讀性過程中接受指導。工程師們報告說，在可讀性過程中，他們與作爲審查員的經驗豐富的谷歌工程師進行了積極的互動。可讀性調查：報告說與可讀性審查員一起工作是可讀性過程的優勢的工程師的比例節奏速度由於可讀性過程，工程師們的工作效率更高。被授予可讀性的工程師判斷自己比沒有被授予可讀性的工程師更有生產力。季度調查：報告他們具有高生產力的工程師的比例工程師們報告說，完成可讀性過程對他們的工程速度有積極的影響。可讀性調查：報告不具備可讀性會降低團隊工程速度的工程師比例由被授予可讀性的工程師編寫的變更列表（）比由未被授予可讀性的工程師編寫的變更列表審查得更快。日誌數據：有可讀性和無可讀性的作者所寫的的審查時間中位數由被授予可讀性的工程師編寫的比由未被授予可讀性的工程師編寫的更容易通過代碼審查。數據：具備可讀性和不具備可讀性的作者編寫的的指導時間的中位數由被授予可讀性的工程師編寫的比由未被授予可讀性的工程師編寫的更快地通過代碼審查。日誌數據：具有可讀性和不具有可讀性的作者的提交時間的中位數可讀性過程不會對工程速度產生負面影響。可讀性調查：報告可讀性過程對其速度有負面影響的工程師比例可讀性調查：報告可讀性審查員及時回覆的工程師比例可讀性調查：可讀性調查：報告審查的及時性是可讀性過程的優勢的工程師比例滿意度工程師們看到了可讀性過程的好處，並對參與這一過程有積極的感受。工程師們認爲可讀性過程是一個總體上積極的經歷可讀性調查：報告說他們在可讀性過程中的經驗總體上是積極的工程師的比例工程師認爲可讀性過程是值得的可讀性調查：報告說可讀性過程是值得的工程師比例可讀性調查：報告稱可讀性審查質量是流程優勢的工程師比例可讀性調查：報道稱徹底性是流程的優勢的工程師比例工程師不認爲可讀性過程是令人沮喪的。可讀性調查：報告說可讀性過程不確定、不清楚、緩慢或令人沮喪的工程師的比例季度調查：報告他們對自己的工程速度感到滿意的工程師的比例

>>>回憶偏差是來自記憶的偏差。人們更願意回憶那些特別有趣或令人沮喪的事件。>>>>近期偏見是另一種形式的來自記憶的偏見，即人們偏向於最近的經歷。在這種情況下，由於他們剛剛成功地完成了這個過程，他們可能會感覺特別好。>>’>>因爲我們只問了那些完成過程的人，所以我們沒有捕捉到那些沒有完成過程的人的意見。>>>>有一種誘惑，就是用這樣的指標來評價個別的工程師，甚至可能用來識別高績效和低績效的人。不過，這樣做會適得其反。如果生產效率指標被用於績效評估，工程師們就會很快學會操弄這些指標，它們將不再對度量和提高整個組織的生產效率有用。讓這些指標發揮作用的唯一方法是，不將其用於度量個體，而是接受度量總體效果。

採取行動並跟蹤結果

“”

回顧我們在本章中的最初目標：我們希望採取行動，提高生產效率。在對某個主題進行研究之後，谷歌的團隊總是準備一份建議清單，說明我們可以如何繼續改進。我們可能會建議給一個工具增加新的功能，改善工具的延遲，改善文檔，刪除過時的流程，甚至改變工程師的激勵結構。理想情況下，這些建議是工具驅動的：如果工具不支持工程師改變他們的流程或思維方式，那麼告訴他們這樣做是沒有用的。相反，我們總是假設，如果工程師有適當的數據和合適的工具可以使用，他們會做出適當的權衡。

就可讀性而言，我們的研究表明，總體上是值得的：實現了可讀性的工程師對這一過程感到滿意，並認爲他們從中學到了東西。我們的記錄顯示，他們的代碼審查得更快，提交得也更快，甚至不再需要那麼多的審查員。我們的研究還顯示了過程中需要改進的地方：工程師們發現了可以使過程更快、更愉快的痛點。語言團隊採納了這些建議，並改進了工具和流程，使其更快、更透明，從而使工程師有一個更愉快的體驗。

總結

’“”

在谷歌，我們發現配備一個工程生產效率專家團隊對軟件工程有廣泛的好處；與其依靠每個團隊制定自己的路線來提高生產效率，一個集中的團隊可以專注於複雜問題的廣泛解決方案。這種以人爲本的因素是出了名的難以度量，而且鑑於改變工程流程所涉及的許多權衡都難以準確度量，而且往往會產生意想不到的後果，因此專家們必須瞭解正在分析的數據。這樣的團隊必須保持數據驅動，旨在消除主觀偏見。

內容提要

’’’’’

在度量生產效率之前，要問結果是否可操作，無論結果是積極還是消極。如果你對這個結果無能爲力，它很可能不值得度量。使用框架選擇有意義的度量標準。一個好的指標是你試圖度量的信號的合理代理，而且它可以追溯到你的原始目標。選擇涵蓋生產效率所有部分的度量標準（）。通過這樣做，你可以確保你不會以犧牲另一個方面（如代碼質量）爲代價來改善生產力的一個方面（如開發人員的速度）。定性指標也是指標。考慮有一個調查機制來跟蹤關於工程師信念的縱向指標。定性指標也應該與定量指標一致；如果它們不一致，很可能是定量指標不正確。爭取創建內置於開發人員工作流程和激勵結構的建議。即使有時有必要推薦額外的培訓或文檔，但如果將其納入開發人員的日常習慣，則更有可能發生變化。