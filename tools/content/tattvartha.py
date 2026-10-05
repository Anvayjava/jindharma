from lib import *

FOOT = ('Digambar recension of the sutras of Acharya Umaswami (33 sutras in chapter 1, 26 in chapter 8). Written from knowledge and compared with a Digambar English/Hindi edition for structure and meaning; the Sanskrit text has not yet been checked letter by letter against a scanned Digambar edition, so each sutra is marked “proofread pending”. Meanings and explanations are written for this site and follow the Sarvarthasiddhi tradition. Please proofread against your own copy.',
        'आचार्य उमास्वामी के सूत्रों का दिगंबर पाठ (अध्याय 1 में 33, अध्याय 8 में 26 सूत्र)। ज्ञान के आधार पर लिखा गया और संरचना तथा अर्थ के लिए एक दिगंबर अंग्रेज़ी/हिन्दी संस्करण से मिलाया गया है; संस्कृत पाठ का स्कैन किए गए किसी दिगंबर संस्करण से अक्षरशः मिलान अभी नहीं हुआ है, इसलिए हर सूत्र "प्रूफ़-पठन शेष" चिह्नित है। अर्थ और व्याख्या इस साइट के लिए सर्वार्थसिद्धि परंपरा के अनुसार लिखे गए हैं। कृपया अपने ग्रंथ से मिलान कर लें।')

def u(no, text, mean, ex, terms=None, title=None, note=None):
    d = dict(no=no, text=text, mean=mean, ex=ex, v='pend', kind='sa')
    if terms: d['terms'] = terms
    if title: d['title'] = title
    if note: d['note'] = note
    return d

def sec(id_, nav, title, intro, units, diagram=''):
    return dict(id=id_, nav=nav, title=title, intro=intro, units=units, diagram=diagram)

def T(*a):
    return a

# ===================== CHAPTER 1 =====================
S = {}
S[1] = u('1.1', "सम्यग्दर्शनज्ञानचारित्राणि मोक्षमार्गः॥",
 ('Right faith, right knowledge and right conduct (together) are the path to liberation.',
  'सम्यग्दर्शन, सम्यग्ज्ञान और सम्यक्चारित्र (तीनों मिलकर) मोक्ष का मार्ग हैं।'),
 ('The first sutra gives the aim of the whole book. The word "marga" (path) is in the <b>singular</b>: the three are not three separate paths but <b>one</b> path, like the three medicines that together cure one disease. Faith alone, knowledge alone or conduct alone cannot give liberation. The order matters: right faith first, because only then does knowledge become right (see 1.31–32), and only right knowledge makes conduct right. Gatha 16 of the Samaysaar looks at the same three from the nishchay view.',
  'पहला सूत्र पूरे ग्रंथ का लक्ष्य बताता है। "मार्गः" शब्द <b>एकवचन</b> में है: तीनों अलग-अलग तीन मार्ग नहीं, बल्कि <b>एक</b> ही मार्ग हैं, जैसे तीन औषधियाँ मिलकर एक रोग मिटाती हैं। अकेली श्रद्धा, अकेला ज्ञान या अकेला चारित्र मोक्ष नहीं दे सकता। क्रम महत्त्वपूर्ण है: पहले सम्यग्दर्शन, क्योंकि तभी ज्ञान सम्यक् होता है (देखें 1.31–32), और सम्यक् ज्ञान से ही चारित्र सम्यक् होता है। समयसार की गाथा 16 इन्हीं तीनों को निश्चय-दृष्टि से देखती है।'),
 terms=[('दर्शन', 'faith, belief', 'श्रद्धा'), ('ज्ञान', 'knowledge', 'ज्ञान'), ('चारित्र', 'conduct', 'आचरण'), ('मोक्षमार्ग', 'path to liberation', 'मोक्ष का मार्ग')],
 title=('The path (ratnatraya)', 'मोक्षमार्ग (रत्नत्रय)'))
S[2] = u('1.2', "तत्त्वार्थश्रद्धानं सम्यग्दर्शनम्॥",
 ('Belief in the tattvas (realities) as they are is right faith.',
  'तत्त्वों के अर्थ (यथार्थ स्वरूप) का श्रद्धान सम्यग्दर्शन है।'),
 ('<b>Tattva</b> = the thing as it is; <b>artha</b> = the object; <b>shraddhan</b> = firm belief. So samyagdarshan is to believe the real nature of the seven tattvas (1.4), without doubt or wrong view. The Digambar tradition adds that this belief is the eight-limbed one (nihshankit etc.) and free from the 25 faults, and that it is attained through true Dev-Shastra-Guru. Compare Samaysaar gatha 11 and 13: there samyaktva is to see the nine padarthas through the bhutartha.',
  '<b>तत्त्व</b> = वस्तु जैसी है; <b>अर्थ</b> = पदार्थ; <b>श्रद्धान</b> = दृढ़ विश्वास। अतः सम्यग्दर्शन सात तत्त्वों (1.4) के यथार्थ स्वरूप पर बिना संशय और विपरीत भाव के श्रद्धा करना है। दिगंबर परंपरा जोड़ती है कि यह श्रद्धा निःशंकित आदि आठ अंगों सहित और पच्चीस दोषों से रहित होती है तथा सच्चे देव-शास्त्र-गुरु के माध्यम से प्राप्त होती है। तुलना करें समयसार गाथा 11 और 13: वहाँ भूतार्थ से नौ पदार्थों को देखना सम्यक्त्व है।'),
 terms=[('तत्त्व', 'tattva: reality, as it is', 'वस्तु का यथार्थ रूप'), ('श्रद्धान', 'firm belief', 'दृढ़ विश्वास')],
 title=('Definition of samyagdarshan', 'सम्यग्दर्शन का लक्षण'))
S[3] = u('1.3', "तन्निसर्गादधिगमाद्वा॥",
 ('That (right faith) arises either by nisarga (naturally) or by adhigam (through acquiring knowledge).',
  'वह (सम्यग्दर्शन) निसर्ग (स्वभाव से) या अधिगम (ज्ञान की प्राप्ति) से उत्पन्न होता है।'),
 ('The two <b>external</b> sources of samyagdarshan. <b>Nisarga</b>: arises on its own, without a teacher in this life, from the effect of past impressions. <b>Adhigam</b>: arises by hearing, studying and understanding the teaching. In both cases the <b>inner</b> cause is the same: the subsiding or destruction of Darshan-mohaniya and Anantanubandhi karma (see the Karma Siddhant page, 4th Gunasthana).',
  'सम्यग्दर्शन के दो <b>बाह्य</b> साधन। <b>निसर्ग</b>: इस जन्म में बिना उपदेश के पूर्व संस्कार के प्रभाव से स्वतः उत्पन्न। <b>अधिगम</b>: उपदेश सुनने, पढ़ने और समझने से उत्पन्न। दोनों में <b>अंतरंग</b> कारण एक ही है: दर्शनमोहनीय और अनंतानुबंधी कर्म का उपशम या क्षय (देखें कर्म सिद्धांत पृष्ठ, चौथा गुणस्थान)।'),
 terms=[('निसर्ग', 'nisarga: natural, without a teacher', 'स्वाभाविक, बिना उपदेश'), ('अधिगम', 'adhigam: by acquiring knowledge', 'ज्ञान प्राप्ति से')],
 title=('Two sources of samyagdarshan', 'सम्यग्दर्शन के दो साधन'))
S[4] = u('1.4', "जीवाजीवास्रवबन्धसंवरनिर्जरामोक्षास्तत्त्वम्॥",
 ('Jiva (soul), ajiva (non-soul), asrav (inflow), bandh (bondage), samvar (stoppage), nirjara (shedding) and moksha (liberation) are the tattvas.',
  'जीव, अजीव, आस्रव, बंध, संवर, निर्जरा और मोक्ष: ये (सात) तत्त्व हैं।'),
 ('These seven are what must be believed in 1.2. They explain the whole story of bondage and release. <b>Jiva</b> and <b>ajiva</b> are the two basic substances. <b>Asrav</b> and <b>bandh</b> explain how the soul becomes bound: this is the cause of the cycle of births. <b>Samvar</b>, <b>nirjara</b> and <b>moksha</b> explain how the soul becomes free. If one tattva is missing the picture is incomplete: with no ajiva we can’t say what binds the soul; with no moksha there is no aim. Adding <b>punya</b> and <b>papa</b> gives the nine padarthas (Samaysaar 13).',
  'ये सात वही हैं जिन पर 1.2 में श्रद्धा करनी है। ये बंध और मुक्ति की पूरी कथा समझाते हैं। <b>जीव</b> और <b>अजीव</b> दो मूल द्रव्य हैं। <b>आस्रव</b> और <b>बंध</b> बताते हैं कि आत्मा कैसे बँधती है: यही संसार-चक्र का कारण है। <b>संवर</b>, <b>निर्जरा</b> और <b>मोक्ष</b> बताते हैं कि आत्मा कैसे मुक्त होती है। एक भी तत्त्व न हो तो चित्र अधूरा: अजीव न हो तो बाँधने वाला क्या है यह नहीं कह सकते; मोक्ष न हो तो लक्ष्य नहीं। पुण्य और पाप जोड़ने पर नौ पदार्थ होते हैं (समयसार 13)।'),
 title=('The seven tattvas', 'सात तत्त्व'))
S[5] = u('1.5', "नामस्थापनाद्रव्यभावतस्तन्न्यासः॥",
 ('Their (the tattvas’, and any object’s) installation (nyasa) is by name, representation, substance and actual state.',
  'उन (तत्त्वों आदि) का न्यास (निक्षेप) नाम, स्थापना, द्रव्य और भाव से होता है।'),
 ('<b>Nikshepa</b> is the way of fixing what a word refers to, so that there is no confusion in speech. For example, the word "Jina": <b>Naam</b>: a boy named "Jinendra". <b>Sthapana</b>: an idol or picture of a Jina (established as a Jina). <b>Dravya</b>: a soul who will become a Jina, or was one (potential, past or future state). <b>Bhava</b>: the actual Arihant, present in the state of being a Jina. All four are used; the bhava-nikshepa is the real one.',
  '<b>निक्षेप</b> शब्द का अर्थ निश्चित करने की पद्धति है, ताकि वाणी में भ्रम न हो। उदाहरण "जिन" शब्द: <b>नाम</b>: जिस बालक का नाम "जिनेंद्र" रखा। <b>स्थापना</b>: जिन की प्रतिमा या चित्र (जिन रूप में स्थापित)। <b>द्रव्य</b>: जो आत्मा जिन होने वाली है या थी (भविष्य या भूत अवस्था)। <b>भाव</b>: वर्तमान में जिन अवस्था में विराजमान साक्षात् अरिहंत। चारों का प्रयोग होता है; भाव-निक्षेप वास्तविक है।'),
 terms=[('न्यास', 'nyasa: installation, nikshepa', 'निक्षेप'), ('स्थापना', 'sthapana: establishing in an image', 'प्रतिमा आदि में स्थापित करना')],
 title=('Four nikshepas', 'चार निक्षेप'))
S[6] = u('1.6', "प्रमाणनयैरधिगमः॥",
 ('Knowledge (of the tattvas) is obtained through pramana and naya.',
  'प्रमाण और नयों से (तत्त्वों का) अधिगम (ज्ञान) होता है।'),
 ('<b>Pramana</b> is knowledge of a thing as a whole (all aspects together). <b>Naya</b> is a view of one aspect while not denying the others. Both are needed: a person who knows only the whole has no detail, and one who knows only one aspect is misled. This is the basis for Anekantavad, which refuses the "only this" of a single view (Chhahdhala Dhal 2, verse 13, calls ekantavad a source of false knowledge).',
  '<b>प्रमाण</b> वस्तु का सम्पूर्ण (सब अंशों सहित) ज्ञान है। <b>नय</b> अन्य अंशों का निषेध किए बिना एक अंश को जानने वाली दृष्टि है। दोनों आवश्यक हैं: जो केवल पूर्ण को जाने उसे विवरण नहीं मिलता, और जो केवल एक अंश जाने वह भ्रम में पड़ता है। यही अनेकांतवाद का आधार है, जो एक दृष्टि के "केवल यही" को नहीं मानता (छहढाला दूसरी ढाल, पद 13, एकांतवाद को मिथ्याज्ञान का कारण कहती है)।'),
 terms=[('प्रमाण', 'pramana: comprehensive valid knowledge', 'वस्तु का सम्पूर्ण यथार्थ ज्ञान'), ('नय', 'naya: viewpoint on one aspect', 'एक अंश को जानने वाली दृष्टि')],
 title=('Pramana and naya', 'प्रमाण और नय'))
S[7] = u('1.7', "निर्देशस्वामित्वसाधनाधिकरणस्थितिविधानतः॥",
 ('(Knowledge is also obtained) by description (nirdesha), ownership (svamitva), cause (sadhana), substratum (adhikarana), duration (sthiti) and division (vidhana).',
  '(अधिगम) निर्देश, स्वामित्व, साधन, अधिकरण, स्थिति और विधान से (भी होता है)।'),
 ('Six questions to ask about any thing. Take samyagdarshan as an example: <b>Nirdesha</b> (what is it?): belief in the tattvas. <b>Svamitva</b> (whose is it?): the soul’s. <b>Sadhana</b> (by what cause?): nisarga or adhigam (1.3). <b>Adhikarana</b> (in what is it?): it is in the soul. <b>Sthiti</b> (how long?): aupashamik lasts an antarmuhurta; kshayik, once gained, is not lost. <b>Vidhana</b> (how many kinds?): three: aupashamik, kshayopashamik, kshayik.',
  'किसी भी वस्तु के बारे में छह प्रश्न। सम्यग्दर्शन को उदाहरण लें: <b>निर्देश</b> (क्या है?): तत्त्वों की श्रद्धा। <b>स्वामित्व</b> (किसका?): आत्मा का। <b>साधन</b> (किस कारण से?): निसर्ग या अधिगम (1.3)। <b>अधिकरण</b> (किसमें?): आत्मा में। <b>स्थिति</b> (कितने समय तक?): औपशमिक अंतर्मुहूर्त तक; क्षायिक एक बार होने पर नष्ट नहीं होता। <b>विधान</b> (कितने प्रकार?): तीन: औपशमिक, क्षायोपशमिक, क्षायिक।'),
 title=('Six ways of knowing', 'ज्ञान के छह द्वार'))
S[8] = u('1.8', "सत्संख्याक्षेत्रस्पर्शनकालान्तरभावाल्पबहुत्वैश्च॥",
 ('And also by existence (sat), number (sankhya), place (kshetra), extent of contact (sparshan), time (kala), interval (antara), state (bhava) and relative smallness or largeness (alpabahutva).',
  'और सत्, संख्या, क्षेत्र, स्पर्शन, काल, अंतर, भाव तथा अल्पबहुत्व से भी (अधिगम होता है)।'),
 ('Eight more ways to know things (the "anuyogadvaras" of the Agam). Example for samyagdarshan: <b>Sat</b>: it exists in jivas from the 4th Gunasthana up. <b>Sankhya</b>: how many jivas have it (some count). <b>Kshetra</b>: the place it occupies (the soul’s pradeshas). <b>Sparshan</b>: how much space it touches. <b>Kala</b>: how long it lasts. <b>Antara</b>: the gap when it is lost and regained. <b>Bhava</b>: which bhava it is (aupashamik, kshayopashamik, kshayik). <b>Alpabahutva</b>: comparison among the three: fewest souls have aupashamik, more have kshayik, and most have kshayopashamik.',
  'वस्तुओं को जानने के आठ और द्वार (आगम के "अनुयोगद्वार")। सम्यग्दर्शन का उदाहरण: <b>सत्</b>: चौथे गुणस्थान से ऊपर के जीवों में है। <b>संख्या</b>: कितने जीवों में है। <b>क्षेत्र</b>: जितने स्थान में रहता है (आत्मा के प्रदेश)। <b>स्पर्शन</b>: कितने क्षेत्र को स्पर्श करता है। <b>काल</b>: कितने समय रहता है। <b>अंतर</b>: छूटने और फिर प्राप्त होने के बीच का अंतराल। <b>भाव</b>: कौन-सा भाव (औपशमिक, क्षायोपशमिक, क्षायिक)। <b>अल्पबहुत्व</b>: तुलना: तीनों में औपशमिक सबसे थोड़े जीवों में, क्षायिक उनसे अधिक में और क्षायोपशमिक सबसे अधिक जीवों में है।'),
 terms=[('सत्', 'sat: existence', 'अस्तित्व'), ('अल्पबहुत्व', 'alpabahutva: comparative number', 'कम-अधिक की तुलना')],
 title=('Eight more ways of knowing', 'ज्ञान के आठ और द्वार'))
S[9] = u('1.9', "मतिश्रुतावधिमनःपर्ययकेवलानि ज्ञानम्॥",
 ('Knowledge (jnana) is of five kinds: mati (sensory), shruta (scriptural), avadhi (clairvoyance), manahparyaya (telepathy) and kevala (omniscience).',
  'ज्ञान पाँच प्रकार का है: मति, श्रुत, अवधि, मनःपर्यय और केवल।'),
 ('The five jnanas form a ladder of increasing purity. <b>Mati</b>: through senses and mind. <b>Shruta</b>: understanding of words and ideas, following mati. <b>Avadhi</b>: direct knowledge of matter within limits. <b>Manahparyaya</b>: direct knowledge of the thoughts of others’ minds. <b>Kevala</b>: knowledge of everything at once, with no obstacle. Each is described in the next sutras. The covering karmas of these five are the five Jnanavaraniya prakritis (see the Karma Siddhant page).',
  'पाँच ज्ञान शुद्धता की बढ़ती सीढ़ी हैं। <b>मति</b>: इंद्रिय और मन से। <b>श्रुत</b>: मतिज्ञान के बाद शब्द और भाव का बोध। <b>अवधि</b>: मर्यादा के भीतर पुद्गल का प्रत्यक्ष ज्ञान। <b>मनःपर्यय</b>: दूसरों के मन के विचारों का प्रत्यक्ष ज्ञान। <b>केवल</b>: सब कुछ एक साथ जानने वाला, बाधा रहित ज्ञान। अगले सूत्रों में प्रत्येक का वर्णन है। इन पाँच के आवरक कर्म पाँच ज्ञानावरणीय प्रकृतियाँ हैं (देखें कर्म सिद्धांत पृष्ठ)।'),
 terms=[('मति', 'sensory knowledge', 'इंद्रिय-मन से ज्ञान'), ('श्रुत', 'scriptural knowledge', 'शास्त्र-ज्ञान'), ('अवधि', 'clairvoyance within limits', 'मर्यादित प्रत्यक्ष ज्ञान'), ('मनःपर्यय', 'telepathy', 'दूसरे के मन का ज्ञान'), ('केवल', 'omniscience', 'सर्वज्ञता')],
 title=('The five jnanas', 'पाँच ज्ञान'))
S[10] = u('1.10', "तत्प्रमाणे॥",
 ('These (five jnanas) are the two pramanas (valid sources of knowledge).',
  'वे (पाँचों ज्ञान) दो प्रमाण हैं।'),
 ('Right knowledge is the pramana, so the five jnanas are divided into two pramanas in the next two sutras: paroksha and pratyaksha. (The wrong kinds of knowledge are covered in 1.31–32.)',
  'सम्यग्ज्ञान ही प्रमाण है, इसलिए अगले दो सूत्रों में पाँचों ज्ञान दो प्रमाणों में बाँटे जाते हैं: परोक्ष और प्रत्यक्ष। (मिथ्या ज्ञान की चर्चा 1.31–32 में है।)'),
 title=('Pramana', 'प्रमाण'))
S[11] = u('1.11', "आद्ये परोक्षम्॥",
 ('The first two (mati and shruta) are paroksha (indirect).',
  'आदि के दो (मति और श्रुत) परोक्ष हैं।'),
 ('<b>Paroksha</b> means "beyond the eye" (para + aksha): knowledge that depends on another, such as the senses, mind, light, or a teacher’s words. The soul does not know directly, but through a medium. That is why mati and shruta may be mistaken.',
  '<b>परोक्ष</b> का अर्थ है "अक्ष से परे" (पर + अक्ष): वह ज्ञान जो किसी दूसरे पर निर्भर है, जैसे इंद्रिय, मन, प्रकाश या गुरु के शब्द। आत्मा सीधे नहीं, माध्यम से जानती है। इसीलिए मति और श्रुत में भूल हो सकती है।'),
 terms=[('परोक्ष', 'paroksha: indirect', 'दूसरे के माध्यम से')],
 title=('Paroksha', 'परोक्ष'))
S[12] = u('1.12', "प्रत्यक्षमन्यत्॥",
 ('The other three (avadhi, manahparyaya, kevala) are pratyaksha (direct).',
  'शेष (तीन: अवधि, मनःपर्यय, केवल) प्रत्यक्ष हैं।'),
 ('<b>Pratyaksha</b>: the soul knows directly, without the senses or mind. Avadhi and manahparyaya are <b>deshapratyaksha</b> (partial, limited). Kevala is <b>sakalapratyaksha</b> (complete). Note the Jain view: what ordinary people call "direct" (seen with the eyes) is only <i>paroksha</i> in the strict sense, because it comes through the senses.',
  '<b>प्रत्यक्ष</b>: आत्मा इंद्रिय या मन के बिना सीधे जानती है। अवधि और मनःपर्यय <b>देश-प्रत्यक्ष</b> (आंशिक, सीमित) हैं। केवल <b>सकल-प्रत्यक्ष</b> (पूर्ण) है। जैन दृष्टि ध्यान रखें: जिसे लोग सामान्यतः "प्रत्यक्ष" (आँख से देखा) कहते हैं, वह कठोर अर्थ में <i>परोक्ष</i> है, क्योंकि वह इंद्रिय से आता है।'),
 terms=[('प्रत्यक्ष', 'pratyaksha: direct', 'सीधा ज्ञान'), ('देशप्रत्यक्ष', 'partial direct knowledge', 'आंशिक प्रत्यक्ष'), ('सकलप्रत्यक्ष', 'complete direct knowledge', 'पूर्ण प्रत्यक्ष')],
 title=('Pratyaksha', 'प्रत्यक्ष'))
S[13] = u('1.13', "मतिः स्मृतिः संज्ञा चिन्ताभिनिबोध इत्यनर्थान्तरम्॥",
 ('Mati, smriti, sanjna, chinta and abhinibodha are synonyms (not different in meaning).',
  'मति, स्मृति, संज्ञा, चिंता और अभिनिबोध: ये अनर्थांतर (एक ही अर्थ वाले, एक ही ज्ञान के भेद-नाम) हैं।'),
 ('These are five forms of Mati-jnana. <b>Smriti</b>: memory (remembering what was seen). <b>Sanjna</b> (also called pratyabhijnana): recognition ("this is the same as that"). <b>Chinta</b> (tarka): reasoning, finding the general rule from cases. <b>Abhinibodha</b> (anumana): inference from a sign (smoke → fire). All depend on the senses and mind, so all are Mati.',
  'ये मतिज्ञान के पाँच रूप हैं। <b>स्मृति</b>: देखे हुए का स्मरण। <b>संज्ञा</b> (प्रत्यभिज्ञान): पहचान ("यह वही है")। <b>चिंता</b> (तर्क): उदाहरणों से सामान्य नियम का निर्णय। <b>अभिनिबोध</b> (अनुमान): चिह्न से ज्ञान (धुआँ → अग्नि)। सब इंद्रिय और मन पर निर्भर हैं, इसलिए सब मतिज्ञान हैं।'),
 terms=[('स्मृति', 'smriti: memory', 'स्मरण'), ('संज्ञा', 'sanjna: recognition', 'पहचान'), ('चिन्ता', 'chinta: reasoning', 'तर्क'), ('अभिनिबोध', 'abhinibodha: inference', 'अनुमान')],
 title=('Forms of mati-jnana', 'मतिज्ञान के रूप'))
S[14] = u('1.14', "तदिन्द्रियानिन्द्रियनिमित्तम्॥",
 ('That (mati) is caused by the senses and by the mind (anindriya).',
  'वह (मतिज्ञान) इंद्रिय और अनिंद्रिय (मन) के निमित्त से होता है।'),
 ('The cause (nimitta) of mati is the five senses (touch, taste, smell, sight, hearing) and the mind (anindriya, literally "not a sense"). So there are six channels of mati: five senses and mind. This is why in 1.16 the count is multiplied by six.',
  'मतिज्ञान के निमित्त पाँच इंद्रियाँ (स्पर्श, रस, गंध, चक्षु, कर्ण) और मन (अनिंद्रिय, अर्थात् "इंद्रिय नहीं") हैं। अतः मतिज्ञान के छह द्वार हैं: पाँच इंद्रियाँ और मन। इसीलिए 1.16 की गणना में छह से गुणा किया जाता है।'),
 terms=[('अनिन्द्रिय', 'anindriya: the mind', 'मन')],
 title=('Causes of mati-jnana', 'मतिज्ञान के निमित्त'))
S[15] = u('1.15', "अवग्रहेहावायधारणाः॥",
 ('(Mati has four stages:) avagraha (grasping), iha (inquiry), avaya (determination) and dharana (retention).',
  '(मतिज्ञान के चार चरण:) अवग्रह, ईहा, अवाय और धारणा।'),
 ('The steps by which a sense-knowledge is formed. Example (hearing): <b>Avagraha</b>: "there is a sound" (first, general grasp). <b>Iha</b>: "is this a conch, or a horn?" (wanting to know more). <b>Avaya</b>: "it is a conch" (decision). <b>Dharana</b>: remembering it later (retention). See the diagram below.',
  'इंद्रिय-ज्ञान बनने के चरण। उदाहरण (सुनना): <b>अवग्रह</b>: "कोई शब्द है" (पहली सामान्य पकड़)। <b>ईहा</b>: "क्या यह शंख है या सींग?" (और जानने की इच्छा)। <b>अवाय</b>: "यह शंख है" (निर्णय)। <b>धारणा</b>: बाद में स्मरण रहना। नीचे का चित्र देखें।'),
 terms=[('अवग्रह', 'avagraha: first grasp', 'प्रारंभिक ग्रहण'), ('ईहा', 'iha: inquiry', 'जिज्ञासा'), ('अवाय', 'avaya: determination', 'निर्णय'), ('धारणा', 'dharana: retention', 'स्मृति में धारण')],
 title=('Four stages', 'चार चरण'))
S[16] = u('1.16', "बहुबहुविधक्षिप्रानिःसृतानुक्तध्रुवाणां सेतराणाम्॥",
 ('(Of these, the knowledge is of) many (bahu), many kinds (bahuvidha), quick (kshipra), unexpressed (anihsrita), unspoken (anukta) and constant (dhruva), along with their opposites (setara).',
  '(इन ज्ञानों के विषय) बहु, बहुविध, क्षिप्र, अनिःसृत, अनुक्त और ध्रुव तथा इनके इतर (विपरीत भेद) हैं।'),
 ('The objects of mati vary in six ways, each with an opposite, so 12 kinds: many / one; many kinds / one kind; quick / slow; hidden (partly seen) / fully expressed; unspoken / spoken; constant / changing. Example: hearing many instruments at once (<i>bahu</i>); knowing that they are of many kinds (<i>bahuvidha</i>); knowing them at once (<i>kshipra</i>). 12 kinds × 4 stages × 6 channels = 288, plus the 48 of 1.18–1.19 = <b>336</b> kinds of mati-jnana (see the table).',
  'मतिज्ञान के विषय छह प्रकार से भिन्न हैं और प्रत्येक का विपरीत भी, अतः 12 भेद: बहु / एक; बहुविध / एकविध; क्षिप्र / अक्षिप्र (धीमा); अनिःसृत (अधूरा दिखा) / निःसृत; अनुक्त / उक्त; ध्रुव / अध्रुव। उदाहरण: एक साथ कई वाद्य सुनना (<i>बहु</i>), यह जानना कि वे अनेक प्रकार के हैं (<i>बहुविध</i>), तुरंत जान लेना (<i>क्षिप्र</i>)। 12 भेद × 4 चरण × 6 द्वार = 288, और 1.18–1.19 के 48 मिलाकर मतिज्ञान के <b>336</b> भेद (सारणी देखें)।'),
 terms=[('बहु', 'many', 'अनेक'), ('क्षिप्र', 'quick', 'शीघ्र'), ('ध्रुव', 'constant', 'स्थिर'), ('सेतर', 'with their opposites', 'विपरीत सहित')],
 title=('Twelve kinds of objects', 'विषय के बारह भेद'))
S[17] = u('1.17', "अर्थस्य॥",
 ('(These four stages apply) to the artha (the manifest object).',
  '(अवग्रह आदि) अर्थ (प्रकट वस्तु) के होते हैं।'),
 ('When the object is clear (<i>artha</i>), all four stages (avagraha, iha, avaya, dharana) occur. The next sutra says what happens when the object is not clear.',
  'जब वस्तु स्पष्ट (<i>अर्थ</i>) हो तो चारों चरण (अवग्रह, ईहा, अवाय, धारणा) होते हैं। अगला सूत्र बताता है कि वस्तु अस्पष्ट हो तो क्या होता है।'),
 title=('Artha', 'अर्थ'))
S[18] = u('1.18', "व्यञ्जनस्यावग्रहः॥",
 ('Of the vyanjana (unmanifest or indistinct object) there is only avagraha.',
  'व्यंजन (अस्पष्ट वस्तु) का केवल अवग्रह होता है।'),
 ('<b>Vyanjana</b> is the initial contact of the object with the sense, before anything is clearly known (like the first drop on a new earthen pot, which only becomes visibly wet after many drops). At this stage there is only avagraha (and not iha, avaya or dharana yet): this is <b>vyanjanavagraha</b>.',
  '<b>व्यंजन</b> वस्तु और इंद्रिय का वह आरंभिक संपर्क है जब तक कुछ स्पष्ट नहीं जाना गया (जैसे नए मिट्टी के बर्तन पर पहली बूँद जो कई बूँदों के बाद ही दिखती है)। इस अवस्था में केवल अवग्रह होता है (ईहा, अवाय, धारणा नहीं): यही <b>व्यंजनावग्रह</b> है।'),
 terms=[('व्यंजन', 'vyanjana: unmanifest object', 'अव्यक्त विषय')],
 title=('Vyanjanavagraha', 'व्यंजनावग्रह'))
S[19] = u('1.19', "न चक्षुरनिन्द्रियाभ्याम्॥",
 ('(Vyanjanavagraha) does not occur through the eye and the mind.',
  '(व्यंजनावग्रह) चक्षु और मन से नहीं होता।'),
 ('The eye and the mind do not touch their object (aprapyakari): they know from a distance. Vyanjanavagraha needs contact, so it is only through the other four senses (touch, taste, smell, hearing). So: 4 senses × 12 kinds = 48 vyanjanavagraha, and 12 × 4 stages × 6 channels = 288 arthavagraha etc. Total 336.',
  'चक्षु और मन अपने विषय को स्पर्श नहीं करते (अप्राप्यकारी): वे दूर से जानते हैं। व्यंजनावग्रह के लिए संपर्क आवश्यक है, इसलिए यह केवल शेष चार इंद्रियों (स्पर्श, रस, गंध, कर्ण) से होता है। अतः 4 इंद्रियाँ × 12 भेद = 48 व्यंजनावग्रह, और 12 × 4 चरण × 6 द्वार = 288। कुल 336।'),
 terms=[('अप्राप्यकारी', 'aprapyakari: knows without touching the object', 'विषय को स्पर्श किए बिना जानने वाला')],
 title=('Which senses', 'किन इंद्रियों से'))
S[20] = u('1.20', "श्रुतं मतिपूर्वं द्व्यनेकद्वादशभेदम्॥",
 ('Shruta follows mati; it is of two kinds, (the second) of many kinds, (the first) of twelve kinds.',
  'श्रुतज्ञान मतिज्ञान-पूर्वक होता है; वह दो प्रकार का है, (एक) अनेक भेद वाला और (दूसरा) बारह भेद वाला।'),
 ('<b>Shruta</b> depends on mati: first the word is heard or read (mati), then its meaning is understood (shruta). It has two main kinds: <b>Anga-bahya</b> (outside the Angas), of many kinds, and <b>Anga-pravishta</b> (inside the Angas), of twelve kinds, the twelve Angas that the Ganadharas compiled from the Tirthankara’s teaching. The 12th Anga is called Drishtivada. (The Digambar tradition holds that the Agam in its fullness has been gradually lost.)',
  '<b>श्रुत</b> मति पर आधारित है: पहले शब्द सुना या पढ़ा जाता है (मति), फिर उसका अर्थ समझा जाता है (श्रुत)। इसके दो मुख्य भेद हैं: <b>अंगबाह्य</b> (अंगों से बाहर), अनेक प्रकार का, और <b>अंगप्रविष्ट</b> (अंगों के भीतर), बारह प्रकार का, अर्थात् बारह अंग जिन्हें गणधरों ने तीर्थंकर की वाणी से रचा। बारहवाँ अंग दृष्टिवाद कहलाता है। (दिगंबर परंपरा मानती है कि मूल आगम पूर्ण रूप में क्रमशः लुप्त हो गया।)'),
 terms=[('अंगबाह्य', 'anga-bahya: outside the twelve Angas', 'बारह अंगों से बाहर'), ('अंगप्रविष्ट', 'anga-pravishta: the twelve Angas', 'बारह अंग')],
 title=('Shruta-jnana', 'श्रुतज्ञान'))
S[21] = u('1.21', "भवप्रत्ययोऽवधिर्देवनारकाणाम्॥",
 ('Avadhi that is caused by birth (bhava-pratyaya) belongs to gods and hell-beings.',
  'भवप्रत्यय अवधिज्ञान देवों और नारकियों को होता है।'),
 ('Gods and hell-beings are born with avadhi-jnana just by being born in that state, without any effort (the "cause" is the birth). Its range differs by their level: higher gods see further. A hell-being with wrong faith has the wrong kind, called <b>vibhanga</b> (1.31): it is what makes them recognise a past enemy (Chhahdhala 1.11).',
  'देव और नारकी उस गति में जन्म लेने मात्र से, बिना प्रयत्न के, अवधिज्ञान के साथ पैदा होते हैं (कारण: जन्म)। इसकी सीमा उनके स्तर के अनुसार भिन्न है: ऊँचे देव अधिक दूर तक देखते हैं। मिथ्यादृष्टि नारकी का अवधि विपरीत होता है, जिसे <b>विभंग</b> कहते हैं (1.31): इसी से वे पूर्व शत्रु को पहचानते हैं (छहढाला 1.11)।'),
 terms=[('भवप्रत्यय', 'caused by birth', 'जन्म से प्राप्त')],
 title=('Avadhi: by birth', 'अवधि: जन्म से'))
S[22] = u('1.22', "क्षयोपशमनिमित्तः षड्विकल्पः शेषाणाम्॥",
 ('For the rest (humans and animals) it is caused by kshayopashama (partial destruction-subsidence of karma), and it is of six kinds.',
  'शेष (मनुष्य और तिर्यंच) जीवों को क्षयोपशम के निमित्त से होता है और यह छह भेद वाला है।'),
 ('For humans and animals, avadhi arises with effort, when the Avadhi-jnanavaraniya karma partly falls away (kshayopashama). It has six forms: <b>Anugami</b> (follows the soul to other places and births), <b>Ananugami</b> (does not follow), <b>Vardhamana</b> (increasing), <b>Hiyamana</b> (decreasing), <b>Avasthita</b> (stays the same), <b>Anavasthita</b> (varies).',
  'मनुष्यों और तिर्यंचों में अवधिज्ञान प्रयत्न से होता है, जब अवधिज्ञानावरणीय कर्म का आंशिक क्षयोपशम होता है। इसके छह रूप हैं: <b>अनुगामी</b> (अन्य स्थान और भव में साथ जाने वाला), <b>अननुगामी</b> (साथ न जाने वाला), <b>वर्धमान</b> (बढ़ता हुआ), <b>हीयमान</b> (घटता हुआ), <b>अवस्थित</b> (वैसा ही रहने वाला), <b>अनवस्थित</b> (घटता-बढ़ता)।'),
 terms=[('क्षयोपशम', 'kshayopashama: partial destruction-subsidence', 'आंशिक क्षय और उपशम')],
 title=('Avadhi: by effort (six kinds)', 'अवधि: प्रयत्न से (छह प्रकार)'))
S[23] = u('1.23', "ऋजुविपुलमती मनःपर्ययः॥",
 ('Manahparyaya has two kinds: rijumati and vipulamati.',
  'मनःपर्यय ज्ञान ऋजुमति और विपुलमति (दो प्रकार का) है।'),
 ('Manahparyaya knows what is in another’s mind. <b>Rijumati</b> (straight): knows thoughts that are simple and clear. <b>Vipulamati</b> (extensive): knows thoughts that are complex, hidden or even those which are only about to be formed.',
  'मनःपर्यय दूसरे के मन में स्थित विचार को जानता है। <b>ऋजुमति</b> (सरल): सरल और स्पष्ट विचारों को जानता है। <b>विपुलमति</b> (विस्तृत): जटिल, गूढ़ या होने वाले विचारों को भी जानता है।'),
 terms=[('ऋजुमति', 'rijumati: simple', 'सरल'), ('विपुलमति', 'vipulamati: extensive', 'विस्तृत')],
 title=('Manahparyaya', 'मनःपर्यय'))
S[24] = u('1.24', "विशुद्ध्यप्रतिपाताभ्यां तद्विशेषः॥",
 ('The difference between the two is in purity (vishuddhi) and in non-falling (apratipata).',
  'उन दोनों का भेद विशुद्धि और अप्रतिपात (न गिरना) से है।'),
 ('Vipulamati is <b>purer</b> than rijumati, and it is <b>apratipati</b>: it does not fall away once gained, until Kevala-jnana. Rijumati may fall (be lost).',
  'विपुलमति ऋजुमति से अधिक <b>विशुद्ध</b> है और <b>अप्रतिपाती</b> भी: एक बार प्राप्त होने पर केवलज्ञान तक नहीं गिरता। ऋजुमति गिर (छूट) भी सकता है।'),
 title=('Rijumati and vipulamati compared', 'ऋजुमति और विपुलमति की तुलना'))
S[25] = u('1.25', "विशुद्धिक्षेत्रस्वामिविषयेभ्योऽवधिमनःपर्याययोः॥",
 ('Avadhi and manahparyaya differ in purity, area, owner and object.',
  'अवधि और मनःपर्यय में विशुद्धि, क्षेत्र, स्वामी और विषय के कारण भेद है।'),
 ('Four differences: <b>Purity</b>: manahparyaya is purer. <b>Area</b>: avadhi can reach much further; manahparyaya is limited to the human region. <b>Owner</b>: avadhi belongs to all four gatis; manahparyaya only to humans, namely a restrained muni with special attainments (riddhi). <b>Object</b>: avadhi knows rupi matter; manahparyaya knows only the thoughts in minds. See the table.',
  'चार भेद: <b>विशुद्धि</b>: मनःपर्यय अधिक विशुद्ध। <b>क्षेत्र</b>: अवधि बहुत दूर तक जा सकता है; मनःपर्यय मनुष्य-क्षेत्र तक सीमित। <b>स्वामी</b>: अवधि चारों गतियों में; मनःपर्यय केवल मनुष्य में, विशेष ऋद्धिधारी संयमी मुनि के। <b>विषय</b>: अवधि रूपी पुद्गल को जानता है; मनःपर्यय केवल मन के विचारों को। सारणी देखें।'),
 title=('Avadhi and manahparyaya compared', 'अवधि और मनःपर्यय की तुलना'))
S[26] = u('1.26', "मतिश्रुतयोर्निबन्धो द्रव्येष्वसर्वपर्यायेषु॥",
 ('The scope (nibandha) of mati and shruta is the dravyas (substances), but not all their paryayas (modes).',
  'मति और श्रुत का विषय-संबंध द्रव्यों में है, पर उनकी सब पर्यायों में नहीं।'),
 ('Mati and shruta can know <b>all six dravyas</b> (the shruta, in words), but only <b>some</b> of the modes of each (not all). We can speak of a soul or of matter, but we cannot know every state of every atom. This sutra starts four sutras (1.26–1.29) that show the scope of the five jnanas, which grows from mati to kevala.',
  'मति और श्रुत <b>छहों द्रव्यों</b> को जान सकते हैं (श्रुत शब्दों द्वारा), पर प्रत्येक की <b>कुछ</b> ही पर्यायें, सब नहीं। हम आत्मा या पुद्गल की चर्चा कर सकते हैं, पर प्रत्येक परमाणु की प्रत्येक अवस्था नहीं जान सकते। यह सूत्र चार सूत्रों (1.26–1.29) की शृंखला आरंभ करता है जो पाँच ज्ञानों का विषय-क्षेत्र दिखाती है, जो मति से केवल तक बढ़ता है।'),
 terms=[('द्रव्य', 'dravya: substance', 'वस्तु'), ('पर्याय', 'paryaya: mode, state', 'अवस्था')],
 title=('Scope of mati and shruta', 'मति-श्रुत का विषय'))
S[27] = u('1.27', "रूपिष्ववधेः॥",
 ('The scope of avadhi is rupi (material) dravyas.',
  'अवधि का विषय रूपी (पुद्गल) द्रव्य हैं।'),
 ('Avadhi knows only <b>rupi</b> dravyas: matter (pudgal), and the soul in its embodied (mixed with karma) state. It does not know the arupi (formless) dravyas like dharma, adharma, akash and kal by itself.',
  'अवधि केवल <b>रूपी</b> द्रव्यों को जानता है: पुद्गल, और कर्म सहित (शरीरधारी) जीव। यह अरूपी द्रव्यों (धर्म, अधर्म, आकाश, काल) को अपने आप नहीं जानता।'),
 terms=[('रूपी', 'rupi: having form (touch, taste, smell, colour)', 'स्पर्श-रस-गंध-वर्ण वाला')],
 title=('Scope of avadhi', 'अवधि का विषय'))
S[28] = u('1.28', "तदनन्तभागे मनःपर्ययस्य॥",
 ('Manahparyaya’s scope is the infinitieth part of that (avadhi’s scope).',
  'मनःपर्यय का विषय उस (अवधि के विषय) के अनंतवें भाग में है।'),
 ('Manahparyaya is far purer but its field is far smaller: it knows only the infinitieth part of what avadhi knows, namely the thoughts (which are matter of a subtle kind) in minds. Purity and breadth are different things.',
  'मनःपर्यय अधिक शुद्ध है पर उसका क्षेत्र बहुत छोटा: वह अवधि के विषय का केवल अनंतवाँ भाग, अर्थात् मन में स्थित (सूक्ष्म पुद्गल रूप) विचारों को जानता है। शुद्धता और विस्तार अलग बातें हैं।'),
 title=('Scope of manahparyaya', 'मनःपर्यय का विषय'))
S[29] = u('1.29', "सर्वद्रव्यपर्यायेषु केवलस्य॥",
 ('The scope of kevala-jnana is all dravyas and all paryayas.',
  'केवलज्ञान का विषय सब द्रव्य और सब पर्यायें हैं।'),
 ('Kevala-jnana knows <b>every substance and every state of it</b>, in all three times, at once. It is the complete knowledge of the Arihant (13th Gunasthana), and arises when the four Ghati karmas are destroyed. Nothing is outside its reach, so there is nothing left to know.',
  'केवलज्ञान <b>सब द्रव्यों और उनकी सब पर्यायों</b> को तीनों कालों में एक साथ जानता है। यह अरिहंत (तेरहवाँ गुणस्थान) का सम्पूर्ण ज्ञान है, जो चार घाती कर्मों के नष्ट होने पर प्रकट होता है। कुछ भी उसके बाहर नहीं, इसलिए जानने को कुछ शेष नहीं।'),
 title=('Scope of kevala-jnana', 'केवलज्ञान का विषय'))
S[30] = u('1.30', "एकादीनि भाज्यानि युगपदेकस्मिन्नाचतुर्भ्यः॥",
 ('One to four jnanas can be present together in one soul (they are to be distributed).',
  'एक आत्मा में एक साथ एक से लेकर चार ज्ञान तक (विभाजित करके) हो सकते हैं।'),
 ('How many jnanas can a soul have at one time? <b>One</b>: only Kevala-jnana (the Arihant). <b>Two</b>: Mati and Shruta (all ordinary people). <b>Three</b>: Mati, Shruta + Avadhi, or Mati, Shruta + Manahparyaya. <b>Four</b>: Mati, Shruta, Avadhi, Manahparyaya. <b>Never five</b>, since Kevala-jnana comes when the others are no longer needed. See the table.',
  'एक आत्मा में एक समय कितने ज्ञान हो सकते हैं? <b>एक</b>: केवल केवलज्ञान (अरिहंत)। <b>दो</b>: मति और श्रुत (सामान्य जन)। <b>तीन</b>: मति, श्रुत और अवधि; या मति, श्रुत और मनःपर्यय। <b>चार</b>: मति, श्रुत, अवधि, मनःपर्यय। <b>पाँच कभी नहीं</b>, क्योंकि केवलज्ञान तब आता है जब शेष ज्ञान की आवश्यकता नहीं रहती। सारणी देखें।'),
 title=('Jnanas in one soul', 'एक आत्मा में ज्ञान'))
S[31] = u('1.31', "मतिश्रुतावधयो विपर्ययश्च॥",
 ('Mati, shruta and avadhi can also be viparyaya (wrong knowledge).',
  'मति, श्रुत और अवधि विपर्यय (मिथ्या) भी होते हैं।'),
 ('The first three jnanas can be right (samyak) or wrong (viparyaya): <b>Kumati</b>, <b>Kushruta</b>, <b>Vibhanga</b> (also called kuavadhi). Manahparyaya and Kevala are always right, since they arise only in a samyagdrishti. This is exactly what Chhahdhala Dhal 2, verse 7 calls "dukhdayak ajnana": knowledge held together with false faith.',
  'पहले तीन ज्ञान सम्यक् भी हो सकते हैं और विपरीत भी: <b>कुमति</b>, <b>कुश्रुत</b>, <b>विभंग</b> (कुअवधि)। मनःपर्यय और केवल सदा सम्यक् हैं, क्योंकि वे सम्यग्दृष्टि को ही होते हैं। यही छहढाला की दूसरी ढाल का पद 7 "दुखदायक अज्ञान" कहता है: मिथ्या श्रद्धा के साथ का ज्ञान।'),
 terms=[('विपर्यय', 'viparyaya: perverse knowledge', 'विपरीत ज्ञान'), ('कुमति', 'kumati: wrong mati', 'मिथ्या मतिज्ञान'), ('विभंग', 'vibhanga: wrong avadhi', 'मिथ्या अवधिज्ञान')],
 title=('Wrong knowledge', 'मिथ्या ज्ञान'))
S[32] = u('1.32', "सदसतोरविशेषाद्यदृच्छोपलब्धेरुन्मत्तवत्॥",
 ('(They are wrong) because there is no distinction between the real (sat) and the unreal (asat), and because knowledge comes by whim (yadrichchha), like that of a mad person.',
  '(वे मिथ्या हैं) क्योंकि सत् और असत् में भेद नहीं करते और यदृच्छा (अपनी इच्छा) से ग्रहण करते हैं, उन्मत्त (पागल) की तरह।'),
 ('This sutra gives the <b>reason</b>: the wrong-believer does not know the real from the unreal, and takes whatever suits him, as a mad man takes the rope for a snake and the snake for a rope. His knowledge is not "wrong in all facts", it is wrong because it has no right standard. Notice the example in Chhahdhala 2.4: "I am the body, my wealth..." is exactly this.',
  'यह सूत्र <b>कारण</b> देता है: मिथ्यादृष्टि सत् और असत् को नहीं पहचानता और जो अपने अनुकूल लगे वही ग्रहण करता है, जैसे पागल रस्सी को साँप और साँप को रस्सी समझ ले। उसका ज्ञान "हर तथ्य में गलत" नहीं, पर इसलिए गलत है कि उसमें सही कसौटी नहीं। छहढाला 2.4 का उदाहरण देखें: "मैं देह हूँ, मेरे धन..." यही है।'),
 terms=[('यदृच्छा', 'yadrichchha: whim, at will', 'अपनी इच्छा से'), ('उन्मत्त', 'unmatta: insane person', 'पागल')],
 title=('Why it is wrong', 'मिथ्या क्यों'))
S[33] = u('1.33', "नैगमसङ्ग्रहव्यवहारर्जुसूत्रशब्दसमभिरूढैवम्भूता नयाः॥",
 ('The nayas (viewpoints) are: Naigama, Sangraha, Vyavahara, Rijusutra, Shabda, Samabhirudha and Evambhuta.',
  'नय (दृष्टिकोण) सात हैं: नैगम, संग्रह, व्यवहार, ऋजुसूत्र, शब्द, समभिरूढ़ और एवंभूत।'),
 ('Seven viewpoints, moving from broad to fine. <b>Naigama</b>: by purpose or intention (a man going to fetch firewood says "I am cooking"). <b>Sangraha</b>: the class as one ("all living beings"). <b>Vyavahara</b>: practical division of the class ("jivas are of two kinds, siddha and samsari"). <b>Rijusutra</b>: only the present moment. <b>Shabda</b>: the word’s grammar and meaning, a changed word has a changed meaning. <b>Samabhirudha</b>: each synonym has its own meaning (Indra, Shakra, Purandara are different aspects). <b>Evambhuta</b>: only while the thing is doing the action named (a "cook" while cooking). The first three are dravyarthika (about substance), the rest paryayarthika (about modes).',
  'सात दृष्टिकोण, स्थूल से सूक्ष्म की ओर। <b>नैगम</b>: संकल्प या प्रयोजन से (लकड़ी लेने जाने वाला कहे "मैं पका रहा हूँ")। <b>संग्रह</b>: जाति को एक मानना ("सभी जीव")। <b>व्यवहार</b>: जाति का व्यावहारिक भेद ("जीव दो प्रकार: सिद्ध और संसारी")। <b>ऋजुसूत्र</b>: केवल वर्तमान क्षण। <b>शब्द</b>: शब्द का व्याकरण और अर्थ, शब्द बदले तो अर्थ बदला। <b>समभिरूढ़</b>: प्रत्येक पर्यायवाची का अपना अर्थ (इंद्र, शक्र, पुरंदर अलग-अलग पक्ष)। <b>एवंभूत</b>: वस्तु जब उसी क्रिया में लगी हो तभी वह नाम (पकाते समय "रसोइया")। पहले तीन द्रव्यार्थिक, शेष पर्यायार्थिक हैं।'),
 terms=[('नय', 'naya: viewpoint', 'दृष्टिकोण'), ('द्रव्यार्थिक', 'dravyarthika: about substance', 'द्रव्य को देखने वाला'), ('पर्यायार्थिक', 'paryayarthika: about modes', 'पर्याय को देखने वाला')],
 title=('Seven nayas', 'सात नय'))

# ---------- chapter 1 diagrams ----------
D_RT = flow([fbox('Samyagdarshan', 'सम्यग्दर्शन', 'gold', ('right faith', 'सही श्रद्धा')), arrow('rd'),
             fbox('Samyagjnan', 'सम्यग्ज्ञान', 'gold', ('right knowledge', 'सही ज्ञान')), arrow('rd'),
             fbox('Samyakcharitra', 'सम्यक्चारित्र', 'gold', ('right conduct', 'सही आचरण')), arrow('rd'),
             fbox('Moksha', 'मोक्ष', 'green', ('liberation', 'मुक्ति'))]) + \
        callout('The word "marga" is singular: the three together are one path. They are the Ratnatraya, “three jewels”. Without the first, knowledge and conduct are not right (1.31–32; Chhahdhala 2.7, 2.14).',
                '"मार्गः" एकवचन है: तीनों मिलकर एक मार्ग हैं। इन्हें रत्नत्रय कहते हैं। पहले के बिना ज्ञान और चारित्र सम्यक् नहीं होते (1.31–32; छहढाला 2.7, 2.14)।', 'info')

D_TATTVA = ('<div class="grid2">' +
  panel(b('Bondage (the cause of the cycle)', 'बंध (संसार का कारण)'),
        flow([fbox('Jiva', 'जीव', 'teal'), fbox('Ajiva', 'अजीव', 'teal'), arrow('rd'), fbox('Asrav', 'आस्रव', 'red'), arrow('rd'), fbox('Bandh', 'बंध', 'red')]), 'red') +
  panel(b('Liberation (the way out)', 'मोक्ष (मुक्ति का मार्ग)'),
        flow([fbox('Samvar', 'संवर', 'green', ('stop inflow', 'आस्रव रोकना')), arrow('rd'), fbox('Nirjara', 'निर्जरा', 'green', ('shed karma', 'कर्म झड़ाना')), arrow('rd'), fbox('Moksha', 'मोक्ष', 'green')]), 'green') +
  '</div>' + callout('Add <b>Punya</b> and <b>Papa</b> to the seven tattvas and you have the nine padarthas (Samaysaar gatha 13).', 'सात तत्त्वों में <b>पुण्य</b> और <b>पाप</b> जोड़ें तो नौ पदार्थ होते हैं (समयसार गाथा 13)।', 'info'))

D_NIK = table([b('Nikshepa', 'निक्षेप'), b('Meaning', 'अर्थ'), b('Example: "Jina"', 'उदाहरण: "जिन"')],
  [[b('Naam', 'नाम'), b('Only a name', 'केवल नाम'), b('A boy called “Jinendra”', 'जिनेंद्र नाम का बालक')],
   [b('Sthapana', 'स्थापना'), b('Established in an image', 'प्रतिमा में स्थापित'), b('A Jina idol or picture', 'जिन प्रतिमा या चित्र')],
   [b('Dravya', 'द्रव्य'), b('Potential, past or future state', 'भूत या भावी अवस्था'), b('A soul who will become, or was, a Jina', 'जो जिन होगा या था')],
   [b('Bhava', 'भाव'), b('Present actual state', 'वर्तमान वास्तविक अवस्था'), b('The living Arihant now', 'वर्तमान में विराजमान अरिहंत')]])

D_ANU = ('<h3>' + b('Samyagdarshan seen through the six (1.7) and the eight (1.8) ways', 'सम्यग्दर्शन छह (1.7) और आठ (1.8) द्वारों से') + '</h3>' +
  table([b('Way', 'द्वार'), b('Question', 'प्रश्न'), b('Answer for samyagdarshan', 'सम्यग्दर्शन के लिए उत्तर')],
   [[b('Nirdesha', 'निर्देश'), b('What is it?', 'क्या है?'), b('Belief in the tattvas', 'तत्त्वों की श्रद्धा')],
    [b('Svamitva', 'स्वामित्व'), b('Whose?', 'किसका?'), b('The soul’s', 'आत्मा का')],
    [b('Sadhana', 'साधन'), b('By what cause?', 'किस कारण से?'), b('Nisarga or adhigam', 'निसर्ग या अधिगम')],
    [b('Adhikarana', 'अधिकरण'), b('In what?', 'किसमें?'), b('In the soul', 'आत्मा में')],
    [b('Sthiti', 'स्थिति'), b('How long?', 'कब तक?'), b('Aupashamik: antarmuhurta; kshayik: not lost', 'औपशमिक: अंतर्मुहूर्त; क्षायिक: नष्ट नहीं')],
    [b('Vidhana', 'विधान'), b('How many kinds?', 'कितने भेद?'), b('Three: aupashamik, kshayopashamik, kshayik', 'तीन: औपशमिक, क्षायोपशमिक, क्षायिक')]]) +
  '<div class="chips">' + ''.join(f'<span class="chip">{b(e, h)}</span>' for e, h in [('Sat', 'सत्'), ('Sankhya', 'संख्या'), ('Kshetra', 'क्षेत्र'), ('Sparshan', 'स्पर्शन'), ('Kala', 'काल'), ('Antara', 'अंतर'), ('Bhava', 'भाव'), ('Alpabahutva', 'अल्पबहुत्व')]) + '</div>')

D_JNAN = ('<div class="flow col">' + fbox('Jnana (Samyagjnana)', 'सम्यग्ज्ञान', 'acc') + '</div>' +
  '<div class="grid2">' +
  panel(b('Paroksha (indirect) · 1.11', 'परोक्ष (अप्रत्यक्ष) · 1.11'), flow([fbox('Mati', 'मति', 'gold', ('senses and mind', 'इंद्रिय और मन')), fbox('Shruta', 'श्रुत', 'gold', ('words and ideas', 'शब्द और भाव'))]), 'gold') +
  panel(b('Pratyaksha (direct) · 1.12', 'प्रत्यक्ष (सीधा) · 1.12'), flow([fbox('Avadhi', 'अवधि', 'teal', ('partial', 'आंशिक')), fbox('Manahparyaya', 'मनःपर्यय', 'teal', ('partial', 'आंशिक')), fbox('Kevala', 'केवल', 'green', ('complete', 'पूर्ण'))]), 'teal') +
  '</div>')

D_MATI = ('<h3>' + b('How a sense-knowledge forms (1.15)', 'इंद्रिय-ज्ञान कैसे बनता है (1.15)') + '</h3>' +
  flow([fbox('Contact: vyanjanavagraha', 'संपर्क: व्यंजनावग्रह', 'gold', ('only 4 senses', 'केवल 4 इंद्रिय')), arrow('rd'),
        fbox('Avagraha', 'अवग्रह', 'acc', ('“a sound”', '“कोई शब्द”')), arrow('rd'),
        fbox('Iha', 'ईहा', 'acc', ('“conch or horn?”', '“शंख या सींग?”')), arrow('rd'),
        fbox('Avaya', 'अवाय', 'acc', ('“a conch”', '“शंख है”')), arrow('rd'),
        fbox('Dharana', 'धारणा', 'green', ('remembered', 'स्मृति में'))]) +
  '<h3>' + b('The 336 kinds of mati-jnana', 'मतिज्ञान के 336 भेद') + '</h3>' +
  table([b('Part', 'भाग'), b('Calculation', 'गणना'), b('Total', 'योग')],
   [[b('Arthavagraha, iha, avaya, dharana', 'अर्थावग्रह, ईहा, अवाय, धारणा'), b('12 kinds × 4 stages × 6 channels (5 senses + mind)', '12 भेद × 4 चरण × 6 द्वार (5 इंद्रिय + मन)'), '288'],
    [b('Vyanjanavagraha', 'व्यंजनावग्रह'), b('12 kinds × 4 senses (not the eye, not the mind)', '12 भेद × 4 इंद्रिय (चक्षु और मन नहीं)'), '48'],
    [b('<b>Total</b>', '<b>कुल</b>'), '288 + 48', '<b>336</b>']]))

D_AVMAN = table([b('', ''), b('Avadhi', 'अवधि'), b('Manahparyaya', 'मनःपर्यय')],
  [[b('Purity', 'विशुद्धि'), b('Less', 'कम'), b('More', 'अधिक')],
   [b('Area (kshetra)', 'क्षेत्र'), b('Very wide', 'बहुत विस्तृत'), b('Limited to the human region', 'मनुष्य-क्षेत्र तक सीमित')],
   [b('Owner (svami)', 'स्वामी'), b('All four gatis', 'चारों गतियाँ'), b('Only a restrained human muni with special attainments', 'केवल संयमी मनुष्य, विशेष ऋद्धि सहित')],
   [b('Object (vishaya)', 'विषय'), b('Rupi dravyas (matter)', 'रूपी द्रव्य (पुद्गल)'), b('Thoughts in minds: the infinitieth part of avadhi’s object', 'मन के विचार: अवधि के विषय का अनंतवाँ भाग')]]) + \
  '<h3>' + b('Rijumati and vipulamati (1.23–1.24)', 'ऋजुमति और विपुलमति (1.23–1.24)') + '</h3>' + \
  table([b('', ''), b('Rijumati', 'ऋजुमति'), b('Vipulamati', 'विपुलमति')],
        [[b('Knows', 'जानता है'), b('Simple, clear thoughts', 'सरल, स्पष्ट विचार'), b('Complex, hidden thoughts', 'जटिल, गूढ़ विचार')],
         [b('Purity', 'विशुद्धि'), b('Less', 'कम'), b('More', 'अधिक')],
         [b('Falls away?', 'छूटता है?'), b('May fall', 'छूट सकता है'), b('Does not fall (apratipati)', 'नहीं छूटता (अप्रतिपाती)')]])

def bars():
    rows = [('Kevala', 'केवल', 100, 'all dravyas, all paryayas', 'सब द्रव्य, सब पर्याय', ''), ('Mati / Shruta', 'मति / श्रुत', 66, 'all dravyas, some paryayas', 'सब द्रव्य, कुछ पर्याय', 'teal'),
            ('Avadhi', 'अवधि', 38, 'rupi dravyas only', 'केवल रूपी द्रव्य', 'red'), ('Manahparyaya', 'मनःपर्यय', 8, '1/∞ of avadhi’s object', 'अवधि के विषय का 1/∞', 'red')]
    s = '<div class="bars">'
    for e, h, w, e2, h2, c in rows:
        s += f'<div class="bar"><span>{b(e, h)}</span><i class="{c}" style="width:{w}%"></i><span>{b(e2, h2)}</span></div>'
    s += '</div>' + callout('Bars show the idea only: they are not to scale. Purity (vishuddhi) is a different measure: manahparyaya is purer than avadhi even though its field is smaller.', 'चित्र केवल भाव दिखाता है, मापनी के अनुसार नहीं है। विशुद्धि अलग माप है: मनःपर्यय का क्षेत्र छोटा होने पर भी वह अवधि से अधिक शुद्ध है।', 'info')
    return s
D_SCOPE = bars()

D_COMBO = table([b('Count', 'संख्या'), b('Which jnanas', 'कौन-से ज्ञान'), b('Who', 'किसमें')],
  [['1', b('Kevala', 'केवल'), b('Arihant, Siddha', 'अरिहंत, सिद्ध')],
   ['2', b('Mati + Shruta', 'मति + श्रुत'), b('Ordinary right-believers', 'सामान्य सम्यग्दृष्टि')],
   ['3', b('Mati + Shruta + Avadhi, or Mati + Shruta + Manahparyaya', 'मति + श्रुत + अवधि, या मति + श्रुत + मनःपर्यय'), b('Gods, hell-beings with avadhi; or munis with manahparyaya', 'अवधिधारी देव-नारकी; या मनःपर्ययधारी मुनि')],
   ['4', b('Mati + Shruta + Avadhi + Manahparyaya', 'मति + श्रुत + अवधि + मनःपर्यय'), b('Munis with both', 'दोनों वाले मुनि')],
   ['5', b('Never together', 'कभी एक साथ नहीं'), b('Kevala comes when the others are no longer needed', 'केवल के आने पर शेष की आवश्यकता नहीं रहती')]])

D_NAYA = ('<div class="flow col">' +
  '<div class="grid2">' +
  panel(b('Dravyarthika (about substance)', 'द्रव्यार्थिक (द्रव्य की दृष्टि)'),
        '<ol><li>' + b('Naigama: by purpose', 'नैगम: प्रयोजन से') + '</li><li>' + b('Sangraha: the class as one', 'संग्रह: जाति को एक मानना') + '</li><li>' + b('Vyavahara: practical division', 'व्यवहार: व्यावहारिक भेद') + '</li></ol>', 'acc') +
  panel(b('Paryayarthika (about modes)', 'पर्यायार्थिक (पर्याय की दृष्टि)'),
        '<ol start="4"><li>' + b('Rijusutra: present moment only', 'ऋजुसूत्र: केवल वर्तमान') + '</li><li>' + b('Shabda: grammar and meaning of the word', 'शब्द: शब्द का व्याकरण और अर्थ') + '</li><li>' + b('Samabhirudha: each synonym its own sense', 'समभिरूढ़: हर पर्याय का अपना अर्थ') + '</li><li>' + b('Evambhuta: only while doing the action', 'एवंभूत: केवल क्रिया के समय') + '</li></ol>', 'teal') +
  '</div></div>' + callout('Broad to fine: each naya narrows the view of the one before it.', 'स्थूल से सूक्ष्म: प्रत्येक नय पिछले की दृष्टि को और संकीर्ण करता है।', 'info'))

CH1 = dict(
    path='tattvartha-sutra/chapter-1.html', title=('Tattvartha Sutra · Chapter 1', 'तत्त्वार्थ सूत्र · अध्याय 1'),
    by=('Acharya Umaswami · Faith and knowledge: the path, the tattvas and the five jnanas', 'आचार्य उमास्वामी · श्रद्धा और ज्ञान: मार्ग, तत्त्व और पाँच ज्ञान'),
    desc='Tattvartha Sutra chapter 1 (33 sutras): Sanskrit text, Hindi and English meaning, diagrams.',
    crumbs=[('tattvartha-sutra/', ('Tattvartha Sutra', 'तत्त्वार्थ सूत्र'))],
    prev=('./', ('Tattvartha Sutra', 'तत्त्वार्थ सूत्र')), next=('chapter-8.html', ('Chapter 8', 'अध्याय 8')),
    foot=FOOT,
    intro='<div class="card">' + bd(
      'Chapter 1 opens the whole text with the aim (1.1), the definition of right faith (1.2–1.8) and the five jnanas (1.9–1.33). It ends with the seven nayas. The sutras are numbered as in the Digambar recension (33 sutras; the Shvetambar recension has 35 and some different wording).',
      'अध्याय 1 पूरे ग्रंथ का लक्ष्य (1.1), सम्यग्दर्शन की परिभाषा (1.2–1.8) और पाँच ज्ञान (1.9–1.33) बताता है, और सात नयों पर समाप्त होता है। सूत्र-संख्या दिगंबर पाठ के अनुसार है (33 सूत्र; श्वेतांबर पाठ में 35 हैं और शब्द कहीं भिन्न हैं)।') + '</div>',
    sections=[
      sec('s1', ('The path', 'मार्ग'), ('The path to liberation (1.1–1.3)', 'मोक्षमार्ग (1.1–1.3)'), None, [S[1], S[2], S[3]], D_RT),
      sec('s2', ('Tattvas', 'तत्त्व'), ('The tattvas and the ways of knowing them (1.4–1.8)', 'तत्त्व और उन्हें जानने के द्वार (1.4–1.8)'), None, [S[4], S[5], S[6], S[7], S[8]], D_TATTVA + D_NIK + D_ANU),
      sec('s3', ('Five jnanas', 'पाँच ज्ञान'), ('The five jnanas and the two pramanas (1.9–1.12)', 'पाँच ज्ञान और दो प्रमाण (1.9–1.12)'), None, [S[9], S[10], S[11], S[12]], D_JNAN),
      sec('s4', ('Mati', 'मति'), ('Mati-jnana (1.13–1.19)', 'मतिज्ञान (1.13–1.19)'), None, [S[i] for i in range(13, 20)], D_MATI),
      sec('s5', ('Shruta, Avadhi, Manah.', 'श्रुत, अवधि, मनः.'), ('Shruta, avadhi and manahparyaya (1.20–1.25)', 'श्रुत, अवधि और मनःपर्यय (1.20–1.25)'), None, [S[i] for i in range(20, 26)], D_AVMAN),
      sec('s6', ('Scope', 'विषय'), ('The scope of the jnanas (1.26–1.30)', 'ज्ञानों का विषय (1.26–1.30)'), None, [S[i] for i in range(26, 31)], D_SCOPE + D_COMBO),
      sec('s7', ('Wrong knowledge', 'मिथ्याज्ञान'), ('Wrong knowledge (1.31–1.32)', 'मिथ्याज्ञान (1.31–1.32)'), None, [S[31], S[32]]),
      sec('s8', ('Nayas', 'नय'), ('The seven nayas (1.33)', 'सात नय (1.33)'), None, [S[33]], D_NAYA),
    ])

# ===================== CHAPTER 8 =====================
K = {}
K[1] = u('8.1', "मिथ्यादर्शनाविरतिप्रमादकषाययोगा बन्धहेतवः॥",
 ('Wrong belief (mithyadarshan), non-restraint (avirati), carelessness (pramada), passions (kashaya) and activity (yoga) are the causes of bondage.',
  'मिथ्यादर्शन, अविरति, प्रमाद, कषाय और योग बंध के हेतु हैं।'),
 ('Five causes in a decreasing order. The first, <b>mithyadarshan</b>, is the root: with it all five operate; without it (4th Gunasthana and above) the first drops out. <b>Avirati</b> goes at the 5th–6th Gunasthana, <b>pramada</b> at the 7th, <b>kashaya</b> at the 10th–11th, and <b>yoga</b> only at the 14th Gunasthana (see the Karma Siddhant page). That is why the Arihant in the 13th stage has only a one-moment bondage of sata-vedaniya.',
  'पाँच कारण घटते क्रम में। पहला, <b>मिथ्यादर्शन</b>, मूल है: उसके रहते पाँचों काम करते हैं; उसके जाने पर (चौथे गुणस्थान से) पहला छूट जाता है। <b>अविरति</b> पाँचवें-छठे गुणस्थान में, <b>प्रमाद</b> सातवें में, <b>कषाय</b> दसवें-ग्यारहवें में, और <b>योग</b> केवल चौदहवें गुणस्थान में छूटता है (देखें कर्म सिद्धांत पृष्ठ)। इसीलिए तेरहवें गुणस्थान के अरिहंत को साता-वेदनीय का केवल एक समय का बंध होता है।'),
 terms=[('प्रमाद', 'pramada: carelessness', 'असावधानी'), ('कषाय', 'kashaya: passions (anger, pride, deceit, greed)', 'क्रोध-मान-माया-लोभ'), ('योग', 'yoga: activity of mind, speech, body', 'मन-वचन-काया की क्रिया')],
 title=('Causes of bondage', 'बंध के हेतु'))
K[2] = u('8.2', "सकषायत्वाज्जीवः कर्मणो योग्यान्पुद्गलानादत्ते स बन्धः॥",
 ('Because of the passions (sakashaya), the jiva takes in the pudgalas suitable for karma. That is bandh.',
  'कषाय सहित होने से जीव कर्म के योग्य पुद्गलों को ग्रहण करता है। वह बंध है।'),
 ('Bondage is not forced from outside: the soul, because it has kashaya, itself <b>takes in</b> karma-matter. Not all pudgala becomes karma, only that "suitable" (<i>karmano yogyan</i>, called karmana-vargana). The definition shows two sides: the soul’s impure bhava (<b>bhava-bandh</b>) and the karma-matter that joins (<b>dravya-bandh</b>), which is explained in the Karma Siddhant page.',
  'बंध बाहर से थोपा हुआ नहीं: कषाय के कारण आत्मा स्वयं कर्म-पुद्गलों को <b>ग्रहण</b> करती है। सारा पुद्गल कर्म नहीं बनता, केवल "योग्य" (<i>कर्मणो योग्यान्</i>, जिसे कार्मण वर्गणा कहते हैं)। परिभाषा के दो पक्ष हैं: आत्मा का मलिन भाव (<b>भाव-बंध</b>) और जुड़ने वाला कर्म-पुद्गल (<b>द्रव्य-बंध</b>), जो कर्म सिद्धांत पृष्ठ में समझाया गया है।'),
 terms=[('आदत्ते', 'takes in', 'ग्रहण करता है'), ('योग्यान्', 'suitable (for karma)', 'योग्य')],
 title=('Definition of bandh', 'बंध की परिभाषा'))
K[3] = u('8.3', "प्रकृतिस्थित्यनुभवप्रदेशास्तद्विधयः॥",
 ('Its (bandh’s) kinds are prakriti (nature), sthiti (duration), anubhava (intensity) and pradesha (quantity).',
  'उस (बंध) के भेद प्रकृति, स्थिति, अनुभव और प्रदेश हैं।'),
 ('The four kinds of bandh, explained by the traditional analogy of a <b>laddu (modak)</b>. <b>Prakriti</b>: its nature (sweet, bitter, which karma). <b>Sthiti</b>: how long it stays unspoiled (duration). <b>Anubhava</b>: how strong the taste (intensity). <b>Pradesha</b>: how big it is (the quantity of particles). Per the Dravyasangraha, yoga decides prakriti and pradesha; kashaya decides sthiti and anubhava.',
  'बंध के चार भेद, परंपरागत <b>लड्डू (मोदक)</b> की उपमा से। <b>प्रकृति</b>: उसका स्वभाव (मीठा, कड़वा; कौन-सा कर्म)। <b>स्थिति</b>: कितने समय तक ठीक रहे। <b>अनुभव</b>: स्वाद कितना तीव्र। <b>प्रदेश</b>: कितना बड़ा (कर्म-कणों की मात्रा)। द्रव्यसंग्रह के अनुसार योग से प्रकृति और प्रदेश बंध, कषाय से स्थिति और अनुभव बंध होता है।'),
 terms=[('प्रकृति', 'prakriti: nature', 'स्वभाव'), ('स्थिति', 'sthiti: duration', 'अवधि'), ('अनुभव', 'anubhava: intensity of fruit', 'फल की तीव्रता'), ('प्रदेश', 'pradesha: quantity of particles', 'कर्म-कणों की मात्रा')],
 title=('Four kinds of bandh', 'बंध के चार भेद'))
K[4] = u('8.4', "आद्यो ज्ञानदर्शनावरणवेदनीयमोहनीयायुर्नामगोत्रान्तरायाः॥",
 ('The first (prakriti-bandh) is of eight kinds: Jnanavarana, Darshanavarana, Vedaniya, Mohaniya, Ayu, Nama, Gotra and Antaraya.',
  'पहला (प्रकृति बंध) आठ प्रकार का है: ज्ञानावरण, दर्शनावरण, वेदनीय, मोहनीय, आयु, नाम, गोत्र और अंतराय।'),
 ('This is the origin of the <b>eight karmas</b> that the Karma Siddhant page studies in detail. "Adya" (the first) means the first of the four kinds in 8.3, prakriti-bandh. These eight divide into four <b>Ghati</b> (Jnanavarana, Darshanavarana, Mohaniya, Antaraya) and four <b>Aghati</b> (Vedaniya, Ayu, Nama, Gotra).',
  'यही वे <b>आठ कर्म</b> हैं जिनका कर्म सिद्धांत पृष्ठ में विस्तार से अध्ययन है। "आद्य" यानी 8.3 के चार भेदों में पहला, प्रकृति-बंध। ये आठ चार <b>घाती</b> (ज्ञानावरण, दर्शनावरण, मोहनीय, अंतराय) और चार <b>अघाती</b> (वेदनीय, आयु, नाम, गोत्र) में बँटते हैं।'),
 title=('The eight prakritis', 'आठ प्रकृतियाँ'))
K[5] = u('8.5', "पञ्चनवद्व्यष्टाविंशतिचतुर्द्विचत्वारिंशद्द्विपञ्चभेदा यथाक्रमम्॥",
 ('(These eight have) five, nine, two, twenty-eight, four, forty-two, two and five divisions respectively.',
  '(इनके) क्रम से पाँच, नौ, दो, अट्ठाईस, चार, बयालीस, दो और पाँच भेद हैं।'),
 ('The numbers 5, 9, 2, 28, 4, 42, 2, 5 add up to <b>97</b> uttara prakritis. Gommatasara counts the Nama karma as 93 (instead of 42) by counting the sub-types, which gives the total <b>148</b> (97 − 42 + 93). So the sutra and the Gommatasara agree; one counts by groups, the other by every sub-type. See the table below and the Karma Siddhant page.',
  'संख्याएँ 5, 9, 2, 28, 4, 42, 2, 5 का योग <b>97</b> उत्तर प्रकृतियाँ है। गोम्मटसार नाम कर्म को 42 की जगह 93 गिनता है (उपभेदों सहित), जिससे कुल <b>148</b> होती हैं (97 − 42 + 93)। अतः सूत्र और गोम्मटसार में विरोध नहीं; एक समूहों से गिनता है, दूसरा हर उपभेद से। नीचे की सारणी और कर्म सिद्धांत पृष्ठ देखें।'),
 title=('The counts: 5, 9, 2, 28, 4, 42, 2, 5', 'संख्याएँ: 5, 9, 2, 28, 4, 42, 2, 5'))
K[6] = u('8.6', "मतिश्रुतावधिमनःपर्ययकेवलानाम्॥",
 ('(The five divisions of Jnanavarana are of) mati, shruta, avadhi, manahparyaya and kevala.',
  '(ज्ञानावरण के पाँच भेद) मति, श्रुत, अवधि, मनःपर्यय और केवल (ज्ञान के आवरक) हैं।'),
 ('Each jnana of chapter 1 (1.9) has its own covering karma. They cover the five jnanas one by one. When the Mati-jnanavarana, for example, is partly removed (kshayopashama) mati-jnana appears; when fully destroyed (kshaya), it is complete.',
  'अध्याय 1 (1.9) के प्रत्येक ज्ञान का अपना आवरक कर्म है। ये पाँच ज्ञानों को एक-एक करके ढकते हैं। जब, उदाहरणार्थ, मतिज्ञानावरण का आंशिक क्षयोपशम होता है तो मतिज्ञान प्रकट होता है; पूर्ण क्षय होने पर वह पूर्ण हो जाता है।'),
 title=('Jnanavaraniya (5)', 'ज्ञानावरणीय (5)'))
K[7] = u('8.7', "चक्षुरचक्षुरवधिकेवलानां निद्रानिद्रानिद्राप्रचलाप्रचलाप्रचलास्त्यानगृद्धयश्च॥",
 ('(The nine of Darshanavarana are) those of chakshu, achakshu, avadhi and kevala (darshan), and Nidra, Nidranidra, Prachala, Prachalaprachala and Styanagriddhi.',
  '(दर्शनावरण के नौ भेद) चक्षु, अचक्षु, अवधि और केवल दर्शन के आवरक, तथा निद्रा, निद्रानिद्रा, प्रचला, प्रचलाप्रचला और स्त्यानगृद्धि।'),
 ('4 darshan-coverings + 5 kinds of sleep = <b>9</b>. The five sleeps get heavier: <i>Nidra</i> (light sleep), <i>Nidranidra</i> (deep sleep), <i>Prachala</i> (sleep while sitting), <i>Prachalaprachala</i> (sleep with drooling, while walking), <i>Styanagriddhi</i> (sleep in which one does acts of great strength).',
  '4 दर्शन-आवरण + 5 निद्राएँ = <b>9</b>। पाँचों निद्राएँ क्रमशः गहरी होती हैं: <i>निद्रा</i> (हल्की), <i>निद्रानिद्रा</i> (गहरी), <i>प्रचला</i> (बैठे-बैठे), <i>प्रचलाप्रचला</i> (चलते हुए, लार टपकते), <i>स्त्यानगृद्धि</i> (जिसमें बड़े पराक्रम के कार्य कर डालता है)।'),
 title=('Darshanavaraniya (9)', 'दर्शनावरणीय (9)'))
K[8] = u('8.8', "सदसद्वेद्ये॥",
 ('The two Vedaniyas are sad-vedya (pleasant) and asad-vedya (unpleasant).',
  'वेदनीय के दो भेद हैं: सद्वेद्य (साता) और असद्वेद्य (असाता)।'),
 ('The two kinds: Sata-vedaniya (pleasant feeling) and Asata-vedaniya (unpleasant feeling). The causes of each are given in chapter 6 (6.11–6.12): sata by compassion, charity, restraint and so on, asata by causing pain, grief and so on. See the Karma Siddhant page.',
  'दो भेद: साता-वेदनीय (सुख का अनुभव) और असाता-वेदनीय (दुःख का अनुभव)। इनके कारण अध्याय 6 (6.11–6.12) में दिए हैं: साता करुणा, दान, संयम आदि से, असाता दुःख, शोक आदि देने से। देखें कर्म सिद्धांत पृष्ठ।'),
 title=('Vedaniya (2)', 'वेदनीय (2)'))
K[9] = u('8.9', "दर्शनचारित्रमोहनीयाकषायकषायवेदनीयाख्यास्त्रिद्विनवषोडशभेदाः सम्यक्त्वमिथ्यात्वतदुभयान्यकषायकषायौ हास्यरत्यरतिशोकभयजुगुप्सास्त्रीपुंनपुंसकवेदा अनन्तानुबन्ध्यप्रत्याख्यानप्रत्याख्यानसंज्वलनविकल्पाश्चैकशः क्रोधमानमायालोभाः॥",
 ('Mohaniya is Darshan-mohaniya and Charitra-mohaniya (the latter being akashaya-vedaniya and kashaya-vedaniya), with 3, 2, 9 and 16 divisions: Samyaktva, Mithyatva and the mixture (tadubhaya) [3]; the Akashaya (9): Hasya, Rati, Arati, Shoka, Bhaya, Jugupsa, the Stri, Purusha and Napumsaka Vedas; and the Kashaya (16): Krodha, Mana, Maya and Lobha, each of the four grades: Anantanubandhi, Apratyakhyana, Pratyakhyana, Samjvalana.',
  'मोहनीय दर्शनमोहनीय और चारित्रमोहनीय है (चारित्रमोहनीय के दो भेद: अकषायवेदनीय और कषायवेदनीय); इनके क्रम से 3, 2, 9 और 16 भेद हैं: सम्यक्त्व, मिथ्यात्व और तदुभय (मिश्र) [3]; अकषाय (9): हास्य, रति, अरति, शोक, भय, जुगुप्सा, स्त्री-, पुरुष- और नपुंसक-वेद; और कषाय (16): क्रोध, मान, माया, लोभ, प्रत्येक के चार स्तर: अनंतानुबंधी, अप्रत्याख्यान, प्रत्याख्यान, संज्वलन।'),
 ('The longest sutra of the chapter. It builds the total of <b>28</b> as: 3 (Darshan-mohaniya) + 9 (akashaya) + 16 (kashaya). The second number "2" in the list refers to the two types of Charitra-mohaniya, not to a count of prakritis. The four grades of kashaya correspond to the Gunasthanas: Anantanubandhi prevents the 4th stage (samyaktva) from arising; Apratyakhyana prevents the 5th; Pratyakhyana the 6th; Samjvalana remains up to the 10th. See the Karma Siddhant page.',
  'अध्याय का सबसे लंबा सूत्र। यह कुल <b>28</b> इस प्रकार बनाता है: 3 (दर्शनमोहनीय) + 9 (अकषाय) + 16 (कषाय)। सूची की संख्या "2" चारित्रमोहनीय के दो प्रकारों की है, प्रकृतियों की गिनती नहीं। कषाय के चार स्तर गुणस्थानों से जुड़ते हैं: अनंतानुबंधी चौथे गुणस्थान (सम्यक्त्व) को उत्पन्न नहीं होने देती; अप्रत्याख्यान पाँचवें को; प्रत्याख्यान छठे को; संज्वलन दसवें तक रहती है। देखें कर्म सिद्धांत पृष्ठ।'),
 terms=[('अकषाय', 'akashaya (nokashaya): minor passions', 'नोकषाय'), ('तदुभय', 'tadubhaya: both (mixed)', 'मिश्र, दोनों')],
 title=('Mohaniya (28)', 'मोहनीय (28)'))
K[10] = u('8.10', "नारकतैर्यग्योनमानुषदैवानि॥",
 ('The four Ayus are of the hell-being (naraka), animal (tiryagyona), human (manushya) and celestial (deva).',
  'आयु (के चार भेद): नारक, तिर्यग्योन, मानुष और देव।'),
 ('Four gatis, four ayus. The causes of each are given in chapter 6 (6.15–6.21); see the Karma Siddhant page for the list. The ayu karma decides how long the soul stays in the body in that gati.',
  'चार गति, चार आयु। प्रत्येक के कारण अध्याय 6 (6.15–6.21) में हैं; सूची के लिए कर्म सिद्धांत पृष्ठ देखें। आयु कर्म तय करता है कि आत्मा उस गति के शरीर में कितना समय रहेगी।'),
 title=('Ayu (4)', 'आयु (4)'))
K[11] = u('8.11', "गतिजातिशरीराङ्गोपाङ्गनिर्माणबन्धनसङ्घातसंस्थानसंहननस्पर्शरसगन्धवर्णानुपूर्व्यगुरुलघूपघातपरघातातपोद्योतोच्छ्वासविहायोगतयः प्रत्येकशरीरत्रससुभगसुस्वरशुभसूक्ष्मपर्याप्तिस्थिरादेययशःकीर्तिसेतराणि तीर्थकरत्वं च॥",
 ('(The Nama karma has these:) gati, jati, sharira, angopanga, nirmana, bandhana, sanghata, samsthana, samhanana, sparsha, rasa, gandha, varna, anupurvya, agurulaghu, upaghata, paraghata, atapa, udyota, ucchvasa, vihayogati; pratyeka-sharira, trasa, subhaga, susvara, shubha, sukshma, paryapti, sthira, adeya and yashahkirti, each with its opposite (setara); and Tirthankaratva.',
  '(नाम कर्म के भेद:) गति, जाति, शरीर, अंगोपांग, निर्माण, बंधन, संघात, संस्थान, संहनन, स्पर्श, रस, गंध, वर्ण, आनुपूर्वी, अगुरुलघु, उपघात, परघात, आतप, उद्योत, उच्छ्वास, विहायोगति; प्रत्येकशरीर, त्रस, सुभग, सुस्वर, शुभ, सूक्ष्म, पर्याप्ति, स्थिर, आदेय और यशःकीर्ति, इन (दस) के प्रतिपक्षी सहित (सेतर); और तीर्थंकरत्व।'),
 ('This is how the sutra counts 42: <b>21</b> (the list from gati to vihayogati) + <b>10</b> (pratyeka-sharira to yashahkirti) + <b>10</b> opposites (setara) + <b>1</b> (Tirthankaratva) = 42. Gommatasara then expands the first group by counting the sub-types (4 gatis, 5 jatis, 5 sharira...) to get 93. Tirthankaratva is the highest auspicious prakriti, bound through the Sixteen Karana Bhavanas (6.24).',
  'सूत्र 42 इस प्रकार गिनता है: <b>21</b> (गति से विहायोगति तक की सूची) + <b>10</b> (प्रत्येकशरीर से यशःकीर्ति तक) + <b>10</b> विपरीत (सेतर) + <b>1</b> (तीर्थंकरत्व) = 42। गोम्मटसार पहले समूह को उपभेदों से गिनकर (4 गति, 5 जाति, 5 शरीर...) 93 करता है। तीर्थंकरत्व सर्वोच्च शुभ प्रकृति है, जो सोलह कारण भावनाओं से बँधती है (6.24)।'),
 title=('Nama (42)', 'नाम (42)'))
K[12] = u('8.12', "उच्चैर्नीचैश्च॥",
 ('Gotra is of two kinds: high (uchcha) and low (nicha).',
  'गोत्र (दो भेद): उच्च और नीच।'),
 ('Uccha-gotra and Nicha-gotra. In Digambar teaching, they are about the family tradition of conduct in which one is born. Chapter 6 (6.25–6.26) says that criticising others and praising oneself bind nicha-gotra, and the reverse, humility and no pride, bind uccha-gotra.',
  'उच्च गोत्र और नीच गोत्र। दिगंबर उपदेश में ये उस कुल-परंपरा के आचरण से संबंधित हैं जिसमें जन्म हो। अध्याय 6 (6.25–6.26) कहता है कि पर-निंदा और आत्म-प्रशंसा से नीच गोत्र बँधता है, और इसका उल्टा, नम्रता और अहंकार-हीनता, उच्च गोत्र बाँधता है।'),
 title=('Gotra (2)', 'गोत्र (2)'))
K[13] = u('8.13', "दानादीनाम्॥",
 ('(The Antaraya karma has five kinds, concerning) dana and the others (labha, bhoga, upabhoga and virya).',
  '(अंतराय के पाँच भेद) दान आदि (दान, लाभ, भोग, उपभोग और वीर्य) के (अंतराय)।'),
 ('"Dana-adi" means: dana (giving), labha (gain), bhoga (single enjoyment), upabhoga (repeated enjoyment), virya (energy). The Antaraya obstructs each of the five. See the Karma Siddhant page.',
  '"दानादि" का अर्थ: दान, लाभ, भोग (एक बार भोगना), उपभोग (बार-बार भोगना) और वीर्य (शक्ति)। अंतराय इन पाँचों में बाधा डालता है। देखें कर्म सिद्धांत पृष्ठ।'),
 title=('Antaraya (5)', 'अंतराय (5)'))
K[14] = u('8.14', "आदितस्तिसृणामन्तरायस्य च त्रिंशत्सागरोपमकोटीकोट्यः परा स्थितिः॥",
 ('The maximum (para) duration of the first three (Jnanavarana, Darshanavarana, Vedaniya) and of the Antaraya is thirty kotakoti sagaropam.',
  'आदि की तीन (ज्ञानावरण, दर्शनावरण, वेदनीय) और अंतराय की उत्कृष्ट स्थिति तीस कोड़ाकोड़ी सागरोपम है।'),
 ('Now sthiti-bandh begins (8.14–8.20). "Aditas tisrinam" means the first three prakritis in the list of 8.4. A <b>sagaropam</b> is an enormous unit of time, and a <b>kotakoti</b> is a crore times a crore of them.',
  'अब स्थिति-बंध (8.14–8.20) आरंभ होता है। "आदितस्तिसृणाम्" का अर्थ 8.4 की सूची की पहली तीन प्रकृतियाँ। <b>सागरोपम</b> समय की अत्यंत विशाल इकाई है, और <b>कोड़ाकोड़ी</b> करोड़ गुणा करोड़ है।'),
 terms=[('सागरोपम', 'sagaropam: a vast unit of time', 'समय की विशाल इकाई'), ('परा', 'para: maximum', 'उत्कृष्ट')],
 title=('Sthiti: 30 kotakoti', 'स्थिति: 30 कोड़ाकोड़ी'))
K[15] = u('8.15', "सप्ततिर्मोहनीयस्य॥",
 ('The maximum duration of Mohaniya is seventy (kotakoti sagaropam).',
  'मोहनीय की उत्कृष्ट स्थिति सत्तर (कोड़ाकोड़ी सागरोपम) है।'),
 ('The longest of the eight, a mark of how powerful Mohaniya is, the king of the eight karmas.',
  'आठों में सबसे लंबी, जो बताती है कि आठ कर्मों का राजा मोहनीय कितना बलवान है।'),
 title=('Mohaniya: 70', 'मोहनीय: 70'))
K[16] = u('8.16', "विंशतिर्नामगोत्रयोः॥",
 ('Twenty (kotakoti sagaropam) is the maximum for Nama and Gotra.',
  'नाम और गोत्र की (उत्कृष्ट स्थिति) बीस (कोड़ाकोड़ी सागरोपम) है।'), ('Nama and Gotra: 20 kotakoti sagaropam.', 'नाम और गोत्र: 20 कोड़ाकोड़ी सागरोपम।'),
 title=('Nama, Gotra: 20', 'नाम, गोत्र: 20'))
K[17] = u('8.17', "त्रयस्त्रिंशत्सागरोपमाण्यायुषः॥",
 ('Thirty-three sagaropam is the maximum for Ayu.',
  'आयु की (उत्कृष्ट स्थिति) तैंतीस सागरोपम है।'),
 ('Ayu is in <b>sagaropam</b>, not kotakoti sagaropam: this matches the 33-sagaropam life of a 7th-hell being or an Anuttara god (see Chhahdhala 1.12, "bahu sagar").',
  'आयु <b>सागरोपम</b> में है, कोड़ाकोड़ी सागरोपम में नहीं: यह सातवें नरक के नारकी या अनुत्तर देव की 33 सागरोपम आयु से मेल खाता है (देखें छहढाला 1.12, "बहु सागर")।'),
 title=('Ayu: 33 sagaropam', 'आयु: 33 सागरोपम'))
K[18] = u('8.18', "अपरा द्वादश मुहूर्ता वेदनीयस्य॥",
 ('The minimum (apara) duration of Vedaniya is twelve muhurtas.',
  'वेदनीय की जघन्य (अपरा) स्थिति बारह मुहूर्त है।'),
 ('The minimum durations begin here. A <b>muhurta</b> is 48 minutes.',
  'जघन्य स्थिति यहाँ से शुरू होती है। एक <b>मुहूर्त</b> 48 मिनट का होता है।'),
 title=('Vedaniya minimum: 12 muhurta', 'वेदनीय जघन्य: 12 मुहूर्त'))
K[19] = u('8.19', "नामगोत्रयोरष्टौ॥",
 ('Eight (muhurtas) for Nama and Gotra.',
  'नाम और गोत्र की (जघन्य स्थिति) आठ (मुहूर्त)।'), ('Nama and Gotra: minimum 8 muhurtas.', 'नाम और गोत्र: जघन्य 8 मुहूर्त।'),
 title=('Nama, Gotra minimum: 8', 'नाम, गोत्र जघन्य: 8'))
K[20] = u('8.20', "शेषाणामन्तर्मुहूर्ता॥",
 ('For the rest, an antarmuhurta.',
  'शेष (कर्मों) की (जघन्य स्थिति) अंतर्मुहूर्त है।'),
 ('The remaining five (Jnanavarana, Darshanavarana, Mohaniya, Ayu, Antaraya) have a minimum of an <b>antarmuhurta</b>, a period of less than 48 minutes.',
  'शेष पाँच (ज्ञानावरण, दर्शनावरण, मोहनीय, आयु, अंतराय) की जघन्य स्थिति <b>अंतर्मुहूर्त</b> है, जो 48 मिनट से कम का समय है।'),
 title=('The rest: antarmuhurta', 'शेष: अंतर्मुहूर्त'))
K[21] = u('8.21', "विपाकोऽनुभवः॥",
 ('Vipaka (fruition) is anubhava (experience).',
  'विपाक (फल का उदय) ही अनुभव (अनुभाग बंध का फल) है।'),
 ('When the karma ripens, the soul feels its result. This is the anubhava-bandh that was defined in 8.3. The intensity (strong or weak) of the fruit is set at the time of bondage by the kashaya.',
  'कर्म पकने पर आत्मा उसका फल अनुभव करती है। यही अनुभव-बंध है जिसकी परिभाषा 8.3 में थी। फल की तीव्रता (तेज़ या मंद) बंध के समय कषाय से तय होती है।'),
 title=('Anubhava', 'अनुभव'))
K[22] = u('8.22', "स यथानाम॥",
 ('That (fruition) is according to the name (of the karma).',
  'वह (विपाक) कर्म के नाम के अनुसार होता है।'),
 ('Each karma gives the fruit its name says: Jnanavarana covers knowledge, Antaraya obstructs, and so on. A karma cannot give the fruit of another karma.',
  'प्रत्येक कर्म अपने नाम के अनुसार फल देता है: ज्ञानावरण ज्ञान को ढकता है, अंतराय बाधा डालता है, इत्यादि। एक कर्म दूसरे कर्म का फल नहीं दे सकता।'),
 title=('Fruit according to name', 'नाम के अनुसार फल'))
K[23] = u('8.23', "ततश्च निर्जरा॥",
 ('And from that (fruition) comes nirjara.',
  'और उससे (फल देने के बाद) निर्जरा होती है।'),
 ('After giving its fruit the karma falls away. This is <b>savipaka nirjara</b> (nirjara by ripening). Nirjara by effort, <b>avipaka nirjara</b>, is by tapa (9.3). See the Karma Siddhant page. Note that if the soul reacts to the fruit with attachment or aversion, new karma is bound: shedding and binding go on together.',
  'फल देने के बाद कर्म झड़ जाता है। यह <b>सविपाक निर्जरा</b> (फल पककर होने वाली) है। प्रयत्न से होने वाली <b>अविपाक निर्जरा</b> तप से होती है (9.3)। देखें कर्म सिद्धांत पृष्ठ। ध्यान दें कि यदि आत्मा फल पर राग-द्वेष से प्रतिक्रिया करे तो नया कर्म बँधता है: झड़ना और बँधना साथ चलते रहते हैं।'),
 title=('Nirjara', 'निर्जरा'))
K[24] = u('8.24', "नामप्रत्ययाः सर्वतो योगविशेषात्सूक्ष्मैकक्षेत्रावगाहस्थिताः सर्वात्मप्रदेशेष्वनन्तानन्तप्रदेशाः॥",
 ('(The pudgalas that make pradesha-bandh are) caused by the nature of each karma (nama-pratyaya); from all directions (sarvatah); by the particular yoga; subtle (sukshma); resting in the same space as the soul (ekakshetra-avagaha); in all the pradeshas of the soul; with infinite-infinite pradeshas (atoms) each.',
  '(प्रदेश-बंध के पुद्गल) प्रत्येक कर्म के नाम के कारण (नामप्रत्यय); सभी ओर से (सर्वतः); योग-विशेष से; सूक्ष्म; आत्मा के साथ एक ही क्षेत्र में ठहरे हुए (एकक्षेत्रावगाह); आत्मा के सभी प्रदेशों में; और अनंतानंत प्रदेश (परमाणु) वाले हैं।'),
 ('Pradesha-bandh described in seven phrases: (1) <b>Nama-pratyaya</b>: the particles are shaped into the eight kinds of karma. (2) <b>Sarvatah</b>: they come from all sides. (3) <b>Yoga-vishesha</b>: the amount depends on the strength of yoga. (4) <b>Sukshma</b>: they are too subtle for the senses. (5) <b>Ekakshetra-avagaha</b>: they occupy the same space-points as the soul. (6) <b>Sarvatma-pradeshu</b>: in every pradesha of the soul (the soul has no part free of karma). (7) <b>Anantananta-pradesha</b>: each bundle contains infinite-infinite atoms. See the picture.',
  'प्रदेश-बंध का वर्णन सात पदों में: (1) <b>नामप्रत्यय</b>: कण आठ प्रकार के कर्म के रूप में ढलते हैं। (2) <b>सर्वतः</b>: सब ओर से आते हैं। (3) <b>योगविशेष</b>: मात्रा योग की शक्ति पर निर्भर। (4) <b>सूक्ष्म</b>: इंद्रियों से जानने योग्य नहीं। (5) <b>एकक्षेत्रावगाह</b>: आत्मा के साथ उन्हीं आकाश-प्रदेशों में ठहरते हैं। (6) <b>सर्वात्मप्रदेशेषु</b>: आत्मा के प्रत्येक प्रदेश में (कोई भाग कर्म से रहित नहीं)। (7) <b>अनंतानंत प्रदेश</b>: प्रत्येक समूह में अनंतानंत परमाणु। चित्र देखें।'),
 terms=[('एकक्षेत्रावगाह', 'occupying the same space', 'एक ही क्षेत्र में ठहरना'), ('योगविशेष', 'specific yoga', 'योग की विशेष शक्ति')],
 title=('Pradesha-bandh', 'प्रदेश-बंध'))
K[25] = u('8.25', "सद्वेद्यशुभायुर्नामगोत्राणि पुण्यम्॥",
 ('Sad-vedya, shubha ayu, shubha nama and shubha gotra are punya.',
  'सद्वेद्य, शुभ आयु, शुभ नाम और शुभ गोत्र पुण्य हैं।'),
 ('Four auspicious prakritis make up <b>punya</b>: Sata-vedaniya, auspicious Ayu (human, celestial, animal), auspicious Nama and high Gotra. They give pleasant results. But note that punya is still <b>bandh</b> (bondage), see Chhahdhala 2.6 and Samaysaar 145 onwards on punya-papa.',
  'चार शुभ प्रकृतियाँ <b>पुण्य</b> हैं: साता-वेदनीय, शुभ आयु (मनुष्य, देव, तिर्यंच), शुभ नाम और उच्च गोत्र। ये सुखद फल देती हैं। पर ध्यान रहे, पुण्य भी <b>बंध</b> ही है, देखें छहढाला 2.6।'),
 title=('Punya', 'पुण्य'))
K[26] = u('8.26', "अतोऽन्यत्पापम्॥",
 ('The others are papa.',
  'इनसे अन्य (शेष कर्म) पाप हैं।'),
 ('The remaining prakritis (all the four Ghati karmas, asata-vedaniya, ashubha ayu, nama and gotra) are <b>papa</b>. Both punya and papa are bondage; liberation needs both to be shed.',
  'शेष प्रकृतियाँ (चारों घाती कर्म, असाता-वेदनीय, अशुभ आयु, नाम और गोत्र) <b>पाप</b> हैं। पुण्य और पाप दोनों बंधन हैं; मोक्ष के लिए दोनों का क्षय आवश्यक है।'),
 title=('Papa', 'पाप'))

# ---------- chapter 8 diagrams ----------
D8_HETU = flow([fbox('Mithyadarshan', 'मिथ्यादर्शन', 'red'), fbox('Avirati', 'अविरति', 'red'), fbox('Pramada', 'प्रमाद', 'red'), fbox('Kashaya', 'कषाय', 'red'), fbox('Yoga', 'योग', 'red'),
                arrow('rd'), fbox('The soul takes in karma-matter (8.2)', 'आत्मा कर्म-पुद्गल ग्रहण करती है (8.2)', 'gold'), arrow('rd'), fbox('Bandh', 'बंध', 'acc')]) + \
          table([b('Cause of bandh', 'बंध का हेतु'), b('Present up to', 'किस गुणस्थान तक'), b('Falls away at', 'कहाँ छूटता है')],
                [[b('Mithyadarshan', 'मिथ्यादर्शन'), '1st (–3rd)', b('4th: with samyagdarshan', '4था: सम्यग्दर्शन होने पर')],
                 [b('Avirati', 'अविरति'), '4th', b('5th–6th: with vows', '5वें–6ठे: व्रत होने पर')],
                 [b('Pramada', 'प्रमाद'), '6th', b('7th', '7वाँ')],
                 [b('Kashaya', 'कषाय'), '10th', b('11th–12th', '11वाँ–12वाँ')],
                 [b('Yoga', 'योग'), '13th', b('14th', '14वाँ')]])

D8_MODAK = ('<div class="grid2">' +
  panel(b('Prakriti (nature)', 'प्रकृति (स्वभाव)'), b('Is the laddu sweet or bitter? Which of the 8 karmas?', 'लड्डू मीठा है या कड़वा? आठ में कौन-सा कर्म?'), 'acc') +
  panel(b('Sthiti (duration)', 'स्थिति (अवधि)'), b('How long does the laddu stay good? How long the karma stays.', 'लड्डू कितने दिन ठीक रहे? कर्म कितने समय रहे।'), 'gold') +
  panel(b('Anubhava (intensity)', 'अनुभव (तीव्रता)'), b('How strong the taste? How intense the fruit.', 'स्वाद कितना तेज़? फल कितना तीव्र।'), 'red') +
  panel(b('Pradesha (quantity)', 'प्रदेश (मात्रा)'), b('How big is the laddu? How many particles.', 'लड्डू कितना बड़ा? कितने कर्म-कण।'), 'teal') +
  '</div>' + flow([fbox('Yoga', 'योग', 'teal'), arrow('rd'), fbox('Prakriti and Pradesha', 'प्रकृति और प्रदेश', 'acc'), fbox('Kashaya', 'कषाय', 'red'), arrow('rd'), fbox('Sthiti and Anubhava', 'स्थिति और अनुभव', 'acc')]))

D8_COUNT = table([b('Karma', 'कर्म'), b('Tattvartha 8.5', 'तत्त्वार्थ 8.5'), b('Gommatasara (satta)', 'गोम्मटसार (सत्ता)')],
  [[b('Jnanavarana', 'ज्ञानावरण'), '5', '5'], [b('Darshanavarana', 'दर्शनावरण'), '9', '9'], [b('Vedaniya', 'वेदनीय'), '2', '2'], [b('Mohaniya', 'मोहनीय'), '28', '28'],
   [b('Ayu', 'आयु'), '4', '4'], [b('Nama', 'नाम'), '42', '93'], [b('Gotra', 'गोत्र'), '2', '2'], [b('Antaraya', 'अंतराय'), '5', '5'],
   [b('<b>Total</b>', '<b>कुल</b>'), '<b>97</b>', '<b>148</b>']]) + \
  callout('The difference of 51 is all in Nama karma (93 − 42): the sutra counts groups, Gommatasara counts every sub-type. Details on the <a href="../karma-siddhant/">Karma Siddhant page</a>.',
          '51 का अंतर पूरा नाम कर्म में है (93 − 42): सूत्र समूह गिनता है, गोम्मटसार हर उपभेद। विवरण <a href="../karma-siddhant/">कर्म सिद्धांत पृष्ठ</a> पर।', 'info')

def sthiti_bars():
    rows = [('Jnanavarana', 'ज्ञानावरण', '30 kotakoti', 30, 'red'), ('Darshanavarana', 'दर्शनावरण', '30 kotakoti', 30, 'red'), ('Vedaniya', 'वेदनीय', '30 kotakoti', 30, 'teal'), ('Mohaniya', 'मोहनीय', '70 kotakoti', 70, 'red'),
            ('Ayu', 'आयु', '33 sagaropam', 8, 'hatch'), ('Nama', 'नाम', '20 kotakoti', 20, 'teal'), ('Gotra', 'गोत्र', '20 kotakoti', 20, 'teal'), ('Antaraya', 'अंतराय', '30 kotakoti', 30, 'red')]
    s = '<div class="bars">'
    for e, h, lab, w, c in rows:
        s += f'<div class="bar"><span>{b(e, h)}</span><i class="{c}" style="width:{w/70*100:.0f}%"></i><span>{lab}</span></div>'
    s += '</div>' + callout('Maximum duration (8.14–8.17). Red = Ghati, teal = Aghati. Ayu is measured in plain sagaropam, not kotakoti sagaropam, so its bar is only a marker (hatched), not to scale.',
                            'उत्कृष्ट स्थिति (8.14–8.17)। लाल = घाती, हरा-नीला = अघाती। आयु सादे सागरोपम में है, कोड़ाकोड़ी सागरोपम में नहीं; इसलिए उसकी पट्टी केवल संकेत (धारीदार) है, मापनी के अनुसार नहीं।', 'info')
    s += table([b('Minimum (jaghanya)', 'जघन्य'), b('Karmas', 'कर्म')],
               [[b('12 muhurta', '12 मुहूर्त'), b('Vedaniya', 'वेदनीय')], [b('8 muhurta', '8 मुहूर्त'), b('Nama, Gotra', 'नाम, गोत्र')],
                [b('Antarmuhurta (< 48 min)', 'अंतर्मुहूर्त (48 मिनट से कम)'), b('Jnanavarana, Darshanavarana, Mohaniya, Ayu, Antaraya', 'ज्ञानावरण, दर्शनावरण, मोहनीय, आयु, अंतराय')]])
    return s
D8_STHITI = sthiti_bars()

def pradesh_svg():
    import math
    s = ['<svg viewBox="0 0 560 330" width="560" role="img" aria-label="Pradesha bandh">',
         '<defs><marker id="pa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" class="ah"/></marker></defs>']
    cx, cy = 280, 165
    for i in range(16):
        a = i * math.pi / 8
        x1, y1 = cx + 145 * math.cos(a), cy + 130 * math.sin(a)
        x2, y2 = cx + 82 * math.cos(a), cy + 76 * math.sin(a)
        s.append(f'<line class="ln" x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" marker-end="url(#pa)"/>')
        s.append(f'<circle cx="{x1:.0f}" cy="{y1:.0f}" r="5" fill="var(--red)"/>')
    s.append(f'<ellipse class="nd gold" cx="{cx}" cy="{cy}" rx="78" ry="72"/>')
    s.append(svgtext(cx, cy - 4, 'Soul', 'आत्मा', 't'))
    s.append(svgtext(cx, cy + 14, 'all pradeshas', 'सभी प्रदेश', 't2'))
    s.append(svgtext(cx, 24, 'Karma-particles come from all sides (sarvatah)', 'कर्म-कण सब ओर से आते हैं (सर्वतः)', 't2'))
    s.append(svgtext(cx, 318, 'Subtle, in the same space-points, in every pradesha', 'सूक्ष्म, उसी क्षेत्र में, हर प्रदेश में', 't2'))
    s.append('</svg>')
    return '<div class="svgbox">' + ''.join(s) + '</div>'
D8_PRAD = pradesh_svg()

D8_PUNYA = ('<div class="grid2">' +
  panel(b('Punya (8.25)', 'पुण्य (8.25)'), '<div class="en"><ul><li>Sata-vedaniya</li><li>Shubha Ayu</li><li>Shubha Nama</li><li>Uccha Gotra</li></ul></div><div class="hi"><ul><li>साता-वेदनीय</li><li>शुभ आयु</li><li>शुभ नाम</li><li>उच्च गोत्र</li></ul></div>', 'green') +
  panel(b('Papa (8.26)', 'पाप (8.26)'), '<div class="en"><ul><li>All four Ghati karmas</li><li>Asata-vedaniya</li><li>Ashubha Ayu, Nama</li><li>Nicha Gotra</li></ul></div><div class="hi"><ul><li>चारों घाती कर्म</li><li>असाता-वेदनीय</li><li>अशुभ आयु, नाम</li><li>नीच गोत्र</li></ul></div>', 'red') +
  '</div>' + callout('Punya and papa are both bandh. Liberation needs the shedding of both (Chhahdhala 2.6).', 'पुण्य और पाप दोनों बंध हैं। मोक्ष के लिए दोनों का क्षय आवश्यक है (छहढाला 2.6)।', 'info'))

CH8 = dict(
    path='tattvartha-sutra/chapter-8.html', title=('Tattvartha Sutra · Chapter 8', 'तत्त्वार्थ सूत्र · अध्याय 8'),
    by=('Acharya Umaswami · Bondage of karma (bandh)', 'आचार्य उमास्वामी · कर्मों का बंध'),
    desc='Tattvartha Sutra chapter 8 (26 sutras): causes and kinds of karma bondage, with diagrams.',
    crumbs=[('tattvartha-sutra/', ('Tattvartha Sutra', 'तत्त्वार्थ सूत्र'))],
    prev=('chapter-1.html', ('Chapter 1', 'अध्याय 1')), next=('./', ('Tattvartha Sutra', 'तत्त्वार्थ सूत्र')),
    foot=FOOT,
    intro='<div class="card">' + bd(
      'Chapter 8 is the source text for the <a href="../karma-siddhant/">Karma Siddhant</a> page: it gives the causes of bondage (8.1–8.2), the four kinds (8.3), the eight karmas and their sub-types (8.4–8.13), the durations (8.14–8.20), fruition and shedding (8.21–8.23), the nature of pradesha-bandh (8.24), and punya and papa (8.25–8.26). The numbering is that of the Digambar recension (26 sutras).',
      'अध्याय 8 <a href="../karma-siddhant/">कर्म सिद्धांत</a> पृष्ठ का मूल-ग्रंथ है: बंध के हेतु (8.1–8.2), चार भेद (8.3), आठ कर्म और उनके उपभेद (8.4–8.13), स्थिति (8.14–8.20), विपाक और निर्जरा (8.21–8.23), प्रदेश-बंध का स्वरूप (8.24), और पुण्य-पाप (8.25–8.26)। क्रमांक दिगंबर पाठ (26 सूत्र) के हैं।') + '</div>',
    sections=[
      sec('s1', ('Causes', 'हेतु'), ('Causes and nature of bondage (8.1–8.3)', 'बंध के हेतु और स्वरूप (8.1–8.3)'), None, [K[1], K[2], K[3]], D8_HETU + D8_MODAK),
      sec('s2', ('Eight karmas', 'आठ कर्म'), ('The eight karmas and their kinds (8.4–8.13)', 'आठ कर्म और उनके भेद (8.4–8.13)'),
          ('A short sutra for each karma. Details in the Karma Siddhant page.', 'प्रत्येक कर्म पर एक संक्षिप्त सूत्र। विवरण कर्म सिद्धांत पृष्ठ में।'), [K[i] for i in range(4, 14)], D8_COUNT),
      sec('s3', ('Sthiti', 'स्थिति'), ('Duration of bondage (8.14–8.20)', 'बंध की स्थिति (8.14–8.20)'), None, [K[i] for i in range(14, 21)], D8_STHITI),
      sec('s4', ('Fruition', 'विपाक'), ('Fruition and nirjara (8.21–8.23)', 'विपाक और निर्जरा (8.21–8.23)'), None, [K[21], K[22], K[23]],
          flow([fbox('Bandh', 'बंध', 'red'), arrow('rd'), fbox('Satta', 'सत्ता', 'gold'), arrow('rd'), fbox('Vipaka (anubhava)', 'विपाक (अनुभव)', 'acc'), arrow('rd'), fbox('Nirjara', 'निर्जरा', 'green')])),
      sec('s5', ('Pradesha', 'प्रदेश'), ('Pradesha-bandh (8.24)', 'प्रदेश-बंध (8.24)'), None, [K[24]], D8_PRAD),
      sec('s6', ('Punya, Papa', 'पुण्य, पाप'), ('Punya and papa (8.25–8.26)', 'पुण्य और पाप (8.25–8.26)'), None, [K[25], K[26]], D8_PUNYA),
    ])

# ===================== HUB =====================
def tile(href, en, hi, sub_en, sub_hi, tag_en, tag_hi, soon=False):
    inner = f'<h3>{b(en, hi)}</h3><p>{b(sub_en, sub_hi)}</p><span class="tag">{b(tag_en, tag_hi)}</span>'
    return f'<div class="tile soon">{inner}</div>' if soon else f'<a class="tile" href="{href}">{inner}</a>'

CHAPTERS = [
 ('chapter-1.html', 'Chapter 1', 'अध्याय 1', 'Faith and knowledge (33 sutras)', 'श्रद्धा और ज्ञान (33 सूत्र)', True),
 ('', 'Chapter 2', 'अध्याय 2', 'The living: jiva (53 sutras)', 'जीव तत्त्व (53 सूत्र)', False),
 ('', 'Chapter 3', 'अध्याय 3', 'The lower and middle worlds (39 sutras)', 'अधोलोक और मध्यलोक (39 सूत्र)', False),
 ('', 'Chapter 4', 'अध्याय 4', 'The celestial beings (42 sutras)', 'देव (42 सूत्र)', False),
 ('', 'Chapter 5', 'अध्याय 5', 'The non-living: ajiva (42 sutras)', 'अजीव तत्त्व (42 सूत्र)', False),
 ('', 'Chapter 6', 'अध्याय 6', 'Asrav: influx of karma (27 sutras)', 'आस्रव (27 सूत्र)', False),
 ('', 'Chapter 7', 'अध्याय 7', 'The five vows (39 sutras)', 'पाँच व्रत (39 सूत्र)', False),
 ('chapter-8.html', 'Chapter 8', 'अध्याय 8', 'Bandh: bondage of karma (26 sutras)', 'बंध तत्त्व (26 सूत्र)', True),
 ('', 'Chapter 9', 'अध्याय 9', 'Samvar and nirjara (47 sutras)', 'संवर और निर्जरा (47 सूत्र)', False),
 ('', 'Chapter 10', 'अध्याय 10', 'Moksha (9 sutras)', 'मोक्ष तत्त्व (9 सूत्र)', False)]
ch_tiles = '<div class="hub">' + ''.join(
    tile(h, e, hi, se, sh, 'Open →' if live else 'Coming soon', 'खोलें →' if live else 'जल्द आ रहा है', not live) for h, e, hi, se, sh, live in CHAPTERS) + '</div>'

HUB = dict(
    path='tattvartha-sutra/index.html', title=('Tattvartha Sutra', 'तत्त्वार्थ सूत्र'),
    by=('Acharya Umaswami · Moksha-shastra · ten chapters on the path to liberation', 'आचार्य उमास्वामी · मोक्षशास्त्र · मोक्षमार्ग पर दस अध्याय'),
    desc='Tattvartha Sutra of Acharya Umaswami: Digambar sutras with Hindi and English explanation.',
    crumbs=[('tattvartha-sutra/', ('Tattvartha Sutra', 'तत्त्वार्थ सूत्र'))], foot=FOOT,
    sections=[dict(id='about', nav=('About', 'परिचय'), title=('About the Tattvartha Sutra', 'तत्त्वार्थ सूत्र परिचय'), intro=None, units=[],
      diagram='<div class="card">' + bd(
        'The <b>Tattvartha Sutra</b> (also <i>Moksha-shastra</i>) by <b>Acharya Umaswami</b> (Umaswati) is the one text accepted by every Jain tradition. It is written in Sanskrit, in short sutras, in <b>ten chapters</b>. It begins with the path to liberation and then explains the seven tattvas one after another. The Digambar recension has 357 sutras, with the classical commentary Sarvarthasiddhi of Acharya Pujyapada. <b>Each page here gives</b> the Sanskrit sutra, its meaning in Hindi and English, explanation, key terms and diagrams.',
        '<b>आचार्य उमास्वामी</b> (उमास्वाति) का <b>तत्त्वार्थ सूत्र</b> (<i>मोक्षशास्त्र</i>) वह एकमात्र ग्रंथ है जो सभी जैन परंपराओं को मान्य है। यह संस्कृत में, संक्षिप्त सूत्रों में, <b>दस अध्यायों</b> में है। यह मोक्षमार्ग से आरंभ करके एक-एक कर सात तत्त्वों को समझाता है। दिगंबर पाठ में 357 सूत्र हैं, और आचार्य पूज्यपाद की सर्वार्थसिद्धि प्रसिद्ध टीका है। <b>यहाँ हर पृष्ठ पर</b> संस्कृत सूत्र, हिन्दी और अंग्रेज़ी अर्थ, व्याख्या, शब्दार्थ और चित्र।') + '</div>'
      + '<h3>' + b('The ten chapters and the seven tattvas', 'दस अध्याय और सात तत्त्व') + '</h3>'
      + table([b('Chapter', 'अध्याय'), b('Subject', 'विषय'), b('Tattva', 'तत्त्व')],
              [['1', b('Path, faith and knowledge', 'मार्ग, श्रद्धा और ज्ञान'), b('(introduction to all seven)', '(सातों का परिचय)')],
               ['2–4', b('Jiva, the lower, middle and upper worlds, the celestial beings', 'जीव, अधो-मध्य-ऊर्ध्व लोक और देव'), b('Jiva', 'जीव')],
               ['5', b('Ajiva (the five non-living dravyas)', 'अजीव (पाँच अजीव द्रव्य)'), b('Ajiva', 'अजीव')],
               ['6–7', b('Influx of karma; the vows', 'कर्मों का आस्रव; व्रत'), b('Asrav', 'आस्रव')],
               ['8', b('Bondage of karma', 'कर्मों का बंध'), b('Bandh', 'बंध')],
               ['9', b('Stoppage and shedding', 'संवर और निर्जरा'), b('Samvar, Nirjara', 'संवर, निर्जरा')],
               ['10', b('Liberation', 'मोक्ष'), b('Moksha', 'मोक्ष')]])
      + '<h3>' + b('Chapters', 'अध्याय') + '</h3>' + ch_tiles)])

PAGES = [HUB, CH1, CH8]
