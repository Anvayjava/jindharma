from lib import *

FOOT = ('Prakrit gathas of Acharya Kundkund, checked line by line against a scanned Digambar edition (Samaysaar with Amritchandra’s Atmakhyati). Gatha 15 follows that edition ("संत"); another commentary reads "सुत्त". Meanings and explanations are written for this site and follow the Atmakhyati tradition. Please proofread against your own copy.',
        'आचार्य कुन्दकुन्द की प्राकृत गाथाएँ, एक स्कैन किए गए दिगंबर संस्करण (अमृतचंद्र की आत्मख्याति सहित समयसार) से पंक्ति-दर-पंक्ति मिलान की गई हैं। गाथा 15 उसी संस्करण ("संत") के अनुसार है; अन्य टीका में "सुत्त" पाठ है। अर्थ और व्याख्या इस साइट के लिए आत्मख्याति परंपरा के अनुसार लिखी गई हैं। कृपया अपने ग्रंथ से मिलान कर लें।')

def u(no, text, mean, ex, terms=None, title=None, note=None):
    d = dict(no=no, text=text, mean=mean, ex=ex, v='ok', kind='pk')
    if terms: d['terms'] = terms
    if title: d['title'] = title
    if note: d['note'] = note
    return d

G = {}
G[1] = u('1', "वंदित्तु सव्वसिद्धे धुवमचलमणोवमं गदिं पत्ते।\nवोच्छामि समयपाहुडमिणमो सुदकेवली भणिदं॥",
 ('Bowing to all the Siddhas, who have attained the firm (dhruv), unmoving (achal) and incomparable (anupam) state, I shall tell this Samaya-prabhrit, as spoken by the Shrutakevalis.',
  'ध्रुव, अचल और अनुपम गति को प्राप्त सभी सिद्धों को नमस्कार करके, श्रुतकेवलियों द्वारा कहे गए इस समयप्राभृत को मैं कहूँगा।'),
 ('The mangalacharan: the author bows to the Siddhas before starting. Each word has a point. <b>Dhruv</b>: the state of the Siddha does not end, unlike the four gatis. <b>Achal</b>: no more wandering. <b>Anupam</b>: nothing in the world can be compared with it. <b>Samaya-prabhrit</b> means the gift (prabhrit) about the true nature of the self (samaya). He bases it on the Shrutakevalis (those who knew the entire Shruta), so this is not his own opinion but the Agam tradition.',
  'मंगलाचरण: ग्रंथ आरंभ करने से पहले आचार्य सिद्धों को नमन करते हैं। हर शब्द का अर्थ है। <b>ध्रुव</b>: सिद्ध अवस्था का अंत नहीं होता, चार गतियों की तरह नहीं। <b>अचल</b>: फिर भटकना नहीं। <b>अनुपम</b>: जगत में उसकी किसी से तुलना नहीं। <b>समयप्राभृत</b> का अर्थ है आत्मा (समय) के सच्चे स्वरूप का उपहार (प्राभृत)। वे श्रुतकेवलियों (सम्पूर्ण श्रुत के ज्ञाता) का आधार लेते हैं, इसलिए यह उनका अपना मत नहीं बल्कि आगम-परंपरा है।'),
 terms=[('धुव', 'dhruv: permanent', 'स्थायी'), ('अचल', 'achal: unmoving', 'अचल'), ('समय', 'samaya: the soul itself', 'आत्मा'), ('पाहुड', 'prabhrit: a treatise as a gift', 'प्राभृत, उपहार-ग्रंथ')],
 title=('Mangalacharan and pratijna', 'मंगलाचरण और प्रतिज्ञा'))
G[2] = u('2', "जीवो चरित्तदंसणणाणट्ठिदो तं हि ससमयं जाण।\nपुग्गलकम्मपदेसट्ठिदं च तं जाण परसमयं॥",
 ('The soul that is established in its own charitra, darshan and jnana, know it to be Svasamay. And the soul that is established in the pradeshas of pudgal-karma, know it to be Parasamay.',
  'जो जीव अपने दर्शन, ज्ञान और चारित्र में स्थित है, उसे ससमय (स्वसमय) जानो। और जो पुद्गल-कर्म के प्रदेशों में स्थित है, उसे परसमय जानो।'),
 ('Samaya is the soul. The gatha splits the soul into two ways of living. <b>Svasamay</b>: it rests in its own nature, knowing and seeing and being steady in itself. <b>Parasamay</b>: it rests in what is not itself, in the feelings produced by karma (moha, raga, dvesha) and so takes the karma-body for the self. The same idea appears in Chhahdhala Dhal 2 as mithyatva: living as if the other (body, karma-effects) were the self.',
  'समय का अर्थ आत्मा है। गाथा आत्मा के जीने के दो प्रकार बताती है। <b>स्वसमय</b>: जो अपने स्वभाव में ठहरा है: ज्ञान, दर्शन और स्वरूप-स्थिरता में। <b>परसमय</b>: जो पर में ठहरा है, यानी कर्म से उत्पन्न मोह-राग-द्वेष भावों में और कर्म-शरीर को अपना मान लेता है। यही बात छहढाला की दूसरी ढाल में मिथ्यात्व के रूप में आई है: पर (शरीर, कर्म-फल) को ही स्व मान लेना।'),
 terms=[('ससमय', 'svasamay: soul in its own nature', 'स्वभाव में स्थित आत्मा'), ('परसमय', 'parasamay: soul absorbed in the other', 'पर में लीन आत्मा'), ('पदेस', 'pradesh: space-points', 'प्रदेश')],
 title=('Svasamay and Parasamay', 'स्वसमय और परसमय'))
G[3] = u('3', "एयत्तणिच्छयगदो समओ सव्वत्थ सुंदरो लोगे।\nबंधकहा एयत्ते तेण विसंवादिणी होदि॥",
 ('The Samaya (soul) that has reached the certainty of oneness (ekatva) is beautiful everywhere in the world. Therefore the story of bondage (bandh) does not agree (is vi-samvadini) with oneness.',
  'एकत्व के निश्चय को प्राप्त समय (आत्मा) लोक में सर्वत्र सुंदर है। इसीलिए एकत्व के साथ बंध की कथा मेल नहीं खाती (विसंवाद उत्पन्न करती है)।'),
 ('<b>Ekatva</b> is the soul’s being one, separate from every other thing. When the soul is understood in this way it is beautiful (sundar), meaning it is free of all blemish. If the soul is only itself, then the story of its being bound, tied, mixed with other things is contradictory. This does not deny bondage in the world, it means that bondage is a story about the soul’s relation with karma, not about the soul’s own nature.',
  '<b>एकत्व</b> का अर्थ है आत्मा का अकेला, सब पर वस्तुओं से भिन्न होना। इस प्रकार समझी गई आत्मा सुंदर है, यानी सब दोषों से रहित। यदि आत्मा केवल स्वयं है तो उसके बँधे होने, मिले होने की कथा उसके साथ मेल नहीं खाती। इसका अर्थ संसार में बंध का निषेध नहीं; अर्थ यह है कि बंध की कथा आत्मा और कर्म के संबंध की कथा है, आत्मा के अपने स्वभाव की नहीं।'),
 terms=[('एयत्त', 'ekatva: oneness, standing alone', 'एकत्व'), ('णिच्छय', 'nishchay: certainty, the real view', 'निश्चय'), ('बंधकहा', 'bandh-katha: the story of bondage', 'बंध की कथा')],
 title=('Ekatva and bandh-katha', 'एकत्व और बंध-कथा'))
G[4] = u('4', "सुदपरिचिदाणुभूदा सव्वस्स वि कामभोगबंधकहा।\nएयत्तस्सुवलंभो णवरि ण सुलहो विहत्तस्स॥",
 ('The story of desire (kama), enjoyment (bhoga) and bondage (bandh) has been heard, become familiar and been experienced by everyone. But attaining the oneness of the soul, separated (vibhakta) from all else, is not easy.',
  'काम, भोग और बंध की कथा सभी ने सुनी है, उससे परिचित हुए हैं और उसका अनुभव किया है। परंतु सबसे भिन्न (विभक्त) आत्मा के एकत्व की प्राप्ति ही सुलभ नहीं है।'),
 ('Why do we need a book like Samaysaar? Because everyone already knows kama-bhoga from heard, familiar, experienced life: "shruta, parichit, anubhut". The soul’s ekatva we have never known. The three words also describe how worldly knowledge gets built: by hearing, by closeness, and by repeated experience. For ekatva we have none of the three.',
  'समयसार जैसे ग्रंथ की आवश्यकता क्यों है? क्योंकि काम-भोग-बंध की कथा तो सबने "श्रुत, परिचित, अनुभूत" जीवन से जान रखी है। आत्मा का एकत्व हमने कभी नहीं जाना। ये तीन शब्द यह भी बताते हैं कि संसारी ज्ञान कैसे बनता है: सुनने से, निकटता से और बार-बार अनुभव से। एकत्व के लिए इन तीनों में से कुछ हमारे पास नहीं।'),
 terms=[('विहत्त', 'vibhakta: separated', 'विभक्त, भिन्न'), ('सुलह', 'easy to get', 'सरलता से प्राप्य')],
 title=('Why ekatva is rare', 'एकत्व दुर्लभ क्यों'))
G[5] = u('5', "तं एयत्तविहत्तं दाएहं अप्पणो सविहवेण।\nजदि दाएज्ज पमाणं चुक्केज्ज छलं ण घेत्तव्वं॥",
 ('I shall show that soul, one and separate (ekatva-vibhakta), with the wealth of my own experience (svavibhav). If I show it, accept it as valid (pramana); if I slip, do not take it as a fault (chhal).',
  'उस एकत्व-विभक्त आत्मा को मैं अपने निज वैभव (स्वानुभव) से दिखाऊँगा। यदि दिखा दूँ तो प्रमाण मानना; यदि चूक जाऊँ तो छल (दोष) ग्रहण मत करना।'),
 ('The author gives his <b>method</b>: he will show the soul from four sources, as commentators explain: the Agam (scripture), yukti (reasoning), the guru-parampara (teachers’ line) and his own svanubhav (self-experience). The humility in the last half is real: if anything is missing, take the sense and not the slip. This is also a good attitude for the student reading: seek the meaning.',
  'आचार्य अपनी <b>पद्धति</b> बताते हैं: टीकाकारों के अनुसार वे चार आधारों से आत्मा को दिखाएँगे: आगम, युक्ति, गुरु-परंपरा और स्वानुभव। अंतिम आधे में विनम्रता सच्ची है: कोई चूक हो तो भाव लेना, चूक नहीं। पढ़ने वाले के लिए भी यह अच्छा दृष्टिकोण है: अर्थ को खोजना।'),
 terms=[('विहव', 'vaibhav: wealth, here self-experience', 'वैभव, यहाँ स्वानुभव'), ('पमाण', 'pramana: valid, authoritative', 'प्रमाण'), ('छल', 'chhal: quibble', 'दोष-ग्रहण')],
 title=('The author’s method', 'आचार्य की पद्धति'))
G[6] = u('6', "ण वि होदि अप्पमत्तो ण पमत्तो जाणओ दु जो भावो।\nएवं भणंति सुद्धं णादो जो सो दु सो चेव॥",
 ('The state that is the knower (jnayak) is neither apramatta (alert) nor pramatta (careless). Thus they call it shuddha (pure). And the one who was known as the knower is that very one only.',
  'जो भाव ज्ञायक है वह न अप्रमत्त है, न प्रमत्त। इसी प्रकार उसे शुद्ध कहते हैं। और जो ज्ञात (ज्ञायक रूप से जाना गया) है, वह वही (ज्ञायक) ही है।'),
 ('Pramatta and apramatta are the 6th and 7th Gunasthanas (see the Karma Siddhant page). The gatha says: the soul as a knower is not these. These names belong to the states of the soul caused by the rise and fall of karma (a view of modifications, <i>paryaya</i>). The knower (jnayak) in its own nature stays the same in all of them. This is the first statement of the <b>nishchay</b> view: the soul seen as the single knower, without division into stages or qualities.',
  'प्रमत्त और अप्रमत्त छठा और सातवाँ गुणस्थान हैं (देखें कर्म सिद्धांत पृष्ठ)। गाथा कहती है: ज्ञायक रूप आत्मा ये नहीं है। ये नाम कर्म के उदय-क्षय से हुई आत्मा की अवस्थाओं (पर्याय-दृष्टि) के हैं। अपने स्वरूप में ज्ञायक सबमें एक-सा रहता है। यह <b>निश्चय</b> दृष्टि का पहला कथन है: आत्मा को एक ज्ञायक के रूप में देखना, बिना अवस्थाओं या गुणों के भेद के।'),
 terms=[('जाणअ', 'jnayak: the knower', 'ज्ञायक, जानने वाला'), ('पमत्त', 'pramatta: careless (6th Gunasthana)', 'छठा गुणस्थान'), ('अप्पमत्त', 'apramatta: alert (7th Gunasthana)', 'सातवाँ गुणस्थान')],
 title=('The Jnayak-bhava', 'ज्ञायक भाव'))
G[7] = u('7', "ववहारेणुवदिस्सइ णाणिस्स चरित्त दंसणं णाणं।\nण वि णाणं ण चरित्तं ण दंसणं जाणगो सुद्धो॥",
 ('By the vyavahar view, charitra, darshan and jnana are taught to the knower. In reality there is neither jnana, nor charitra, nor darshan: there is only the pure knower (jnayak).',
  'व्यवहार से ज्ञानी (शिष्य) को चारित्र, दर्शन और ज्ञान का उपदेश दिया जाता है। निश्चय से न ज्ञान है, न चारित्र, न दर्शन: केवल शुद्ध ज्ञायक है।'),
 ('This is one of the most quoted gathas. It does <b>not</b> say that darshan, jnana and charitra are worthless. It says they are separate "names" or "divisions" that are used to teach a single, indivisible soul. In practice (vyavahar) the student must be told to have faith, knowledge and conduct. When he understands what the teaching points to, he sees there is one jnayak. See gatha 16 for how both fit together.',
  'यह सर्वाधिक उद्धृत की जाने वाली गाथाओं में से एक है। यह <b>नहीं</b> कहती कि दर्शन, ज्ञान, चारित्र व्यर्थ हैं। यह कहती है कि ये एक अखंड आत्मा को समझाने के लिए प्रयुक्त अलग-अलग "नाम" या "भेद" हैं। व्यवहार में शिष्य को श्रद्धा, ज्ञान और आचरण का उपदेश देना आवश्यक है। जब वह समझता है कि उपदेश किस ओर संकेत करता है, तब उसे एक ज्ञायक दिखता है। दोनों कैसे मिलते हैं, यह गाथा 16 में देखें।'),
 terms=[('ववहार', 'vyavahar: the practical, divided view', 'व्यवहार, भेद-दृष्टि'), ('सुद्ध', 'shuddha: pure', 'शुद्ध')],
 title=('Vyavahar teaching', 'व्यवहार से उपदेश'))
G[8] = u('8', "जह ण वि सक्कमणज्जो अणज्जभासं विणा दु गाहेदुं।\nतह ववहारेण विणा परमत्थुवदेसणमसक्कं॥",
 ('Just as a non-Aryan (a person who knows only a local language) cannot be made to understand without his own language, so without vyavahar it is not possible to teach the paramartha (the highest truth).',
  'जैसे अनार्य (केवल अपनी बोली जानने वाला) को उसकी भाषा के बिना कुछ समझाना संभव नहीं, वैसे ही व्यवहार के बिना परमार्थ का उपदेश देना संभव नहीं।'),
 ('The analogy of language. A teacher must speak the language of the listener, even if it is not the truest language. Vyavahar (division, naming, stages like Gunasthanas) is that language; paramartha (the single, pure soul) is the meaning. So the Samaysaar does not reject vyavahar: it uses it as a ladder, as the rest of Jain teaching does. After reaching the top one knows what the ladder was for.',
  'भाषा की उपमा। उपदेशक को श्रोता की भाषा में बोलना पड़ता है, चाहे वह सबसे सच्ची भाषा न हो। व्यवहार (भेद, नाम, गुणस्थान आदि अवस्थाएँ) वही भाषा है; परमार्थ (अखंड शुद्ध आत्मा) अर्थ है। अतः समयसार व्यवहार को नकारता नहीं: जैसे शेष जैन उपदेश करता है, वैसे वह उसे सीढ़ी की तरह प्रयोग करता है। शिखर पर पहुँचकर पता चलता है कि सीढ़ी किस काम की थी।'),
 terms=[('अणज्ज', 'anarya: a speaker of another language', 'दूसरी भाषा बोलने वाला'), ('परमत्थ', 'paramartha: the highest truth', 'परमार्थ')],
 title=('Why vyavahar is needed', 'व्यवहार आवश्यक क्यों'))
G[9] = u('9', "जो हि सुदेणहिगच्छदि अप्पाणमिणं तु केवलं सुद्धं।\nतं सुदकेवलिमिसिणो भणंति लोयप्पदीवयरा॥",
 ('He who, through the Shruta (scripture), knows this soul as pure and alone (kevala): the sages, the lamps of the world, call him a Shrutakevali.',
  'जो श्रुत के द्वारा इस आत्मा को केवल (अकेला) और शुद्ध जानता है, उसे लोक को प्रकाशित करने वाले ऋषि श्रुतकेवली कहते हैं।'),
 ('The test of true scripture study: it ends in knowing the soul pure and alone. The usual meaning of Shrutakevali is a monk who knows all the Agam. Here the gatha gives an inner (nishchay) meaning: whoever knows the soul by the scripture is a Shrutakevali in the sense that matters.',
  'सच्चे शास्त्र-अध्ययन की कसौटी: वह आत्मा को शुद्ध और अकेली जानने में समाप्त हो। श्रुतकेवली का सामान्य अर्थ है वह मुनि जो समस्त आगम जानता हो। यहाँ गाथा आंतरिक (निश्चय) अर्थ देती है: जो शास्त्र से आत्मा को जानता है, वह उस अर्थ में श्रुतकेवली है जो वास्तव में महत्त्वपूर्ण है।'),
 terms=[('सुदकेवली', 'shrutakevali', 'श्रुतकेवली'), ('लोयप्पदीवयर', 'lamp-makers of the world (illuminators)', 'लोक को प्रकाशित करने वाले')],
 title=('The Shrutakevali (inner meaning)', 'श्रुतकेवली (निश्चय अर्थ)'))
G[10] = u('10', "जो सुदणाणं सव्वं जाणदि सुदकेवलिं तमाहु जिणा।\nणाणं अप्पा सव्वं जम्हा सुदकेवली तम्हा॥",
 ('He who knows all the Shruta-jnana, the Jinas call him a Shrutakevali (this is the vyavahar meaning). And because all knowledge is the soul, therefore (the one who knows the soul) is a Shrutakevali (this is the nishchay meaning).',
  'जो समस्त श्रुतज्ञान को जानता है उसे जिनेन्द्र श्रुतकेवली कहते हैं (यह व्यवहार अर्थ है)। और क्योंकि सारा ज्ञान आत्मा ही है, इसलिए (आत्मा को जानने वाला) श्रुतकेवली है (यह निश्चय अर्थ है)।'),
 ('Gatha 10 puts the vyavahar and nishchay meanings of Shrutakevali next to each other: the Jinas call the knower of all the Shruta a Shrutakevali, and from the inner view knowing the soul is the same as knowing the whole of knowledge, since knowledge is the soul itself. A good example of the two views not contradicting each other.',
  'गाथा 10 श्रुतकेवली के व्यवहार और निश्चय अर्थ साथ-साथ रखती है: जिनेन्द्र समस्त श्रुत के ज्ञाता को श्रुतकेवली कहते हैं, और आंतरिक दृष्टि से आत्मा को जानना समस्त ज्ञान को जानने के बराबर है, क्योंकि ज्ञान स्वयं आत्मा है। दोनों दृष्टियाँ परस्पर विरोधी नहीं, इसका अच्छा उदाहरण।'),
 title=('Two meanings of Shrutakevali', 'श्रुतकेवली के दो अर्थ'))
G[11] = u('11', "ववहारोऽभूदत्थो भूदत्थो देसिदो दु सुद्धणओ।\nभूदत्थमस्सिदो खलु सम्मादिट्ठी हवदि जीवो॥",
 ('Vyavahar is abhutartha (not the real); the shuddha-naya is taught as bhutartha (the real). The jiva who has taken shelter of the bhutartha is indeed a samyagdrishti (a right-believer).',
  'व्यवहार अभूतार्थ (जो वस्तु का वास्तविक रूप नहीं) है; शुद्धनय भूतार्थ (वास्तविक) कहा गया है। जो जीव भूतार्थ का आश्रय करता है, वह निश्चय ही सम्यग्दृष्टि होता है।'),
 ('The key gatha of the Samaysaar. <b>Bhutartha</b> means "the thing as it is" and <b>abhutartha</b> "not the thing as it is". Vyavahar describes the soul with divisions (stages, qualities) and mixed with karma; the shuddha-naya describes the soul as it is in itself. The commentator’s image: <i>jala-kardama</i>. In muddy water, the water and the mud are mixed; if one pays attention to the water by itself, one sees it clear. Taking shelter (ashraya) of bhutartha is the true meaning of samyagdarshan in Samaysaar. (Compare Tattvartha Sutra 1.2: faith in tattvas as they are.)',
  'समयसार की मूल गाथा। <b>भूतार्थ</b> का अर्थ है "वस्तु जैसी है वैसी" और <b>अभूतार्थ</b> "वस्तु जैसी नहीं"। व्यवहार आत्मा का वर्णन भेदों (अवस्था, गुण) और कर्म के मेल सहित करता है; शुद्धनय आत्मा का वर्णन उसके अपने स्वरूप में करता है। टीकाकार की उपमा: <i>जल-कर्दम</i>। मिट्टी मिले जल में जल और कीचड़ मिले होते हैं; यदि जल को अलग देखा जाए तो वह निर्मल दिखता है। भूतार्थ का आश्रय करना ही समयसार में सम्यग्दर्शन का सच्चा अर्थ है। (तुलना: तत्त्वार्थ सूत्र 1.2, तत्त्वों का यथार्थ श्रद्धान।)'),
 terms=[('भूदत्थ', 'bhutartha: the real, as it is', 'यथार्थ'), ('अभूदत्थ', 'abhutartha: not the real', 'अयथार्थ'), ('सम्मादिट्ठि', 'samyagdrishti: right-believer', 'सम्यग्दृष्टि')],
 title=('Bhutartha and abhutartha', 'भूतार्थ और अभूतार्थ'))
G[12] = u('12', "सुद्धो सुद्धादेसो णादव्वो परमभावदरिसीहिं।\nववहारदेसिदा पुण जे दु अपरमे ट्ठिदा भावे॥",
 ('The shuddha-naya (shuddha-adesh) is to be known by those who see the supreme state (paramabhava). But those who stand in a lower state (aparama bhava) are taught by the vyavahar.',
  'जो परमभाव को देखने वाले हैं, उनके लिए शुद्ध (शुद्धादेश, शुद्धनय) जानने योग्य है। परंतु जो अपरम (निम्न) भाव में स्थित हैं, उन्हें व्यवहार से उपदेश दिया जाता है।'),
 ('Who needs which naya? A person who has reached the highest steadiness (paramabhava) is taught by the shuddha-naya; the one who is at a lower level is taught by vyavahar: that is, he follows vows, pratimas, charitra and so on. This confirms gatha 8: vyavahar has its place. The failing is to stay at vyavahar and think it is all, or to claim to have reached the top without having climbed.',
  'किसे कौन-सा नय? जो परम भाव (उच्च स्थिरता) में पहुँच चुका है उसे शुद्धनय से समझाया जाता है; जो निचले स्तर पर है उसे व्यवहार से: अर्थात् वह व्रत, प्रतिमा, चारित्र आदि का पालन करे। यह गाथा 8 की पुष्टि है: व्यवहार का अपना स्थान है। दोष यह है कि कोई व्यवहार पर ही ठहर जाए और उसी को सब माने, या बिना चढ़े शिखर पर पहुँचने का दावा करे।'),
 terms=[('परमभाव', 'paramabhava: highest state', 'उत्कृष्ट अवस्था'), ('अपरम', 'aparama: lower', 'निम्न')],
 title=('Who needs which naya', 'किसे कौन-सा नय'))
G[13] = u('13', "भूदत्थेणाभिगदा जीवाजीवा य पुण्णपावं च।\nआसवसंवरणिज्जर बंधो मोक्खो य सम्मत्तं॥",
 ('The jiva, ajiva, punya, papa, asrav, samvar, nirjara, bandh and moksha, when known by the bhutartha, is samyaktva (right faith).',
  'जीव, अजीव, पुण्य, पाप, आस्रव, संवर, निर्जरा, बंध और मोक्ष, इन नौ पदार्थों को जब भूतार्थ (शुद्धनय) से जाना जाता है, वह सम्यक्त्व है।'),
 ('The nine padarthas are the seven tattvas of Tattvartha Sutra 1.4 plus punya and papa. When they are seen through the bhutartha (the shuddha-naya) the soul sees itself as the real jiva, and everything else as ajiva or as modifications caused by karma. That understanding is samyaktva. This links the Samaysaar to the Tattvartha Sutra (1.2 and 1.4) and to Chhahdhala Dhal 2, which explained how each tattva is wrongly seen.',
  'नौ पदार्थ वे सात तत्त्व हैं जो तत्त्वार्थ सूत्र 1.4 में हैं, साथ में पुण्य और पाप। जब इन्हें भूतार्थ (शुद्धनय) से देखा जाता है, तब आत्मा स्वयं को वास्तविक जीव और शेष सबको अजीव या कर्मजन्य पर्यायें देखती है। वही समझ सम्यक्त्व है। यह समयसार को तत्त्वार्थ सूत्र (1.2, 1.4) और छहढाला की दूसरी ढाल से जोड़ती है, जहाँ हर तत्त्व को ग़लत रूप से देखने की बात बताई गई थी।'),
 terms=[('पदार्थ', 'padartha: the nine categories', 'नौ पदार्थ')],
 title=('Nine padarthas and samyaktva', 'नौ पदार्थ और सम्यक्त्व'))
G[14] = u('14', "जो पस्सदि अप्पाणं अबद्धपुट्ठं अणण्णयं णियदं।\nअविसेसमसंजुत्तं तं सुद्धणयं वियाणीहि॥",
 ('He who sees the soul as abaddha-sprishta (unbound, untouched), ananya (not different from itself), niyat (constant), avisesh (without distinctions) and asanyukta (not joined): know that to be the shuddha-naya.',
  'जो आत्मा को अबद्धस्पृष्ट (न बँधा, न छुआ हुआ), अनन्य (अन्य रूप न होने वाला), नियत (स्थिर), अविशेष (भेद रहित) और असंयुक्त (मिला नहीं) देखता है, उसे शुद्धनय जानो।'),
 ('Gatha 14 gives the five marks of the soul seen by the shuddha-naya: (1) <b>Abaddha-sprishta</b>: it is not bound by karma and not in contact with it (in its own nature). (2) <b>Ananya</b>: not turning into any other substance or state. (3) <b>Niyat</b>: constant, not changing its nature in any state. (4) <b>Avisesh</b>: no divisions like knowledge, faith, conduct, or high and low. (5) <b>Asanyukta</b>: not joined with ragadi bhavas. See the picture.',
  'गाथा 14 शुद्धनय से देखी गई आत्मा के पाँच लक्षण देती है: (1) <b>अबद्धस्पृष्ट</b>: अपने स्वरूप में कर्म से न बँधी, न उसके स्पर्श में। (2) <b>अनन्य</b>: किसी अन्य द्रव्य या अवस्था रूप न होने वाली। (3) <b>नियत</b>: स्थिर, किसी भी अवस्था में स्वभाव न बदलने वाली। (4) <b>अविशेष</b>: ज्ञान, श्रद्धा, चारित्र, ऊँच-नीच आदि भेदों से रहित। (5) <b>असंयुक्त</b>: रागादि भावों से मिली नहीं। चित्र देखें।'),
 terms=[('अबद्धपुट्ठ', 'abaddha-sprishta: unbound, untouched', 'न बँधा, न स्पर्शित'), ('अणण्ण', 'ananya: not another', 'दूसरा नहीं बनने वाला'), ('णियद', 'niyat: fixed', 'स्थिर'), ('अविसेस', 'avisesh: undivided', 'भेद रहित'), ('असंजुत्त', 'asanyukta: unjoined', 'असंयुक्त')],
 title=('Five marks of the shuddha-naya', 'शुद्धनय के पाँच लक्षण'))
G[15] = u('15', "जो पस्सदि अप्पाणं अबद्धपुट्ठं अणण्णमविसेसं।\nअपदेससंतमज्झं पस्सदि जिणसासणं सव्वं॥",
 ('He who sees the soul as unbound, untouched, not another and without distinctions, that one sees the entire Jina-shasana (the teaching of the Jinas).',
  'जो आत्मा को अबद्धस्पृष्ट, अनन्य और अविशेष देखता है, वह समस्त जिनशासन को देखता है।'),
 ('The strongest claim in the section: seeing the pure soul is seeing the whole Jain teaching. The phrase "apadesa-santa-majjham" is explained by the commentator as "in the midst of dravya-shruta (the words of scripture) and bhava-shruta (the knowledge it gives)". The sense: all scripture, in its words and in its knowledge, points to this one thing. The reading "sutta" in Jayasena’s commentary would mean "in the midst of the sutra". Both readings give the same sense.',
  'इस खंड का सबसे सशक्त कथन: शुद्ध आत्मा को देखना समस्त जैन शासन को देखना है। "अपदेससंतमज्झं" की टीकाकार यह व्याख्या करते हैं: "द्रव्यश्रुत (शास्त्र के शब्द) और भावश्रुत (उनसे मिले ज्ञान) के मध्य"। भाव यह कि पूरा शास्त्र, अपने शब्दों में भी और ज्ञान में भी, इसी एक वस्तु की ओर संकेत करता है। जयसेन की टीका के "सुत्त" पाठ का अर्थ होता है "सूत्र के मध्य"। दोनों पाठों का भाव एक ही है।'),
 terms=[('जिणसासण', 'Jina-shasana: the Jain teaching', 'जिन-शासन')],
 title=('Seeing the whole Jina-shasana', 'सम्पूर्ण जिनशासन का दर्शन'),
 note=('Reading note: this edition has "संत"; the Jayasena commentary reads "सुत्त".', 'पाठ-टिप्पणी: इस संस्करण में "संत"; जयसेन की टीका में "सुत्त"।'))
G[16] = u('16', "दंसणणाणचरित्ताणि सेविदव्वाणि साहुणा णिच्चं।\nताणि पुण जाण तिण्णि वि अप्पाणं चेव णिच्छयदो॥",
 ('Darshan, jnana and charitra should be constantly followed by the sadhu. But know those three to be indeed the soul itself, from the nishchay view.',
  'साधु को दर्शन, ज्ञान और चारित्र का निरंतर सेवन करना चाहिए। परंतु उन तीनों को निश्चय से आत्मा ही जानो।'),
 ('Gatha 16 puts together everything so far. The sadhu follows the three jewels (<b>vyavahar</b>: the practice, Tattvartha Sutra 1.1). Yet at the same time he knows the three are not outside the soul: they are the soul (<b>nishchay</b>). That is the way to read gatha 7 correctly: the nishchay view does not drop the practice, it shows what the practice is. Two views, one path.',
  'गाथा 16 अब तक की सारी बात एकत्र करती है। साधु रत्नत्रय का सेवन करता है (<b>व्यवहार</b>: आचरण, तत्त्वार्थ सूत्र 1.1)। साथ ही वह जानता है कि ये तीनों आत्मा से बाहर नहीं, आत्मा ही हैं (<b>निश्चय</b>)। गाथा 7 को सही पढ़ने का यही तरीका है: निश्चय-दृष्टि आचरण को छोड़ती नहीं, बताती है कि आचरण क्या है। दो दृष्टियाँ, एक मार्ग।'),
 terms=[('साहु', 'sadhu: the monk', 'साधु'), ('णिच्छयदो', 'by the nishchay view', 'निश्चय से')],
 title=('Ratnatraya: practice and essence', 'रत्नत्रय: आचरण और सार'))

def sec(id_, nav, title, intro, units, diagram=''):
    return dict(id=id_, nav=nav, title=title, intro=intro, units=units, diagram=diagram)

# ---- diagrams ----
ADHIKARS = [
 ('Purvarang', 'पूर्वरंग', '1–38', 'acc'), ('Jiva-Ajiva', 'जीवाजीव', '39–68', 'teal'), ('Karta-Karma', 'कर्ता-कर्म', '69–144', 'teal'),
 ('Punya-Papa', 'पुण्य-पाप', '145–163', 'teal'), ('Asrav', 'आस्रव', '164–180', 'red'), ('Samvar', 'संवर', '181–192', 'green'),
 ('Nirjara', 'निर्जरा', '193–236', 'green'), ('Bandh', 'बंध', '237–287', 'red'), ('Moksha', 'मोक्ष', '288–307', 'green'),
 ('Sarvavishuddha-jnana', 'सर्वविशुद्ध ज्ञान', '308–415', 'gold')]
adh = '<div class="flow">' + ''.join(fbox(e, h, c, (f'gathas {g}', f'गाथा {g}')) for e, h, g, c in ADHIKARS) + '</div>'
adh += callout('Total: 415 gathas (38 + 30 + 76 + 19 + 17 + 12 + 44 + 51 + 20 + 108), following Amritchandra’s Atmakhyati. This page covers gathas 1–16 of the Purvarang.',
               'कुल 415 गाथाएँ (38 + 30 + 76 + 19 + 17 + 12 + 44 + 51 + 20 + 108), अमृतचंद्र की आत्मख्याति के अनुसार। यह पृष्ठ पूर्वरंग की गाथा 1–16 पर है।', 'info')

svasamay = ('<div class="grid2">' +
  panel(b('Svasamay', 'स्वसमय'), '<div class="en">The soul <b>established in its own darshan, jnana and charitra</b>. It rests in what it is. Peace, knowing, steadiness.</div><div class="hi">आत्मा <b>अपने दर्शन, ज्ञान और चारित्र में स्थित</b>। वह जो है उसी में ठहरी है। शांति, ज्ञान, स्थिरता।</div>', 'green') +
  panel(b('Parasamay', 'परसमय'), '<div class="en">The soul <b>established in the pradeshas of pudgal-karma</b>: lost in moha, raga, dvesha, which are the other’s effects. Restlessness, wandering.</div><div class="hi">आत्मा <b>पुद्गल-कर्म के प्रदेशों में स्थित</b>: मोह, राग, द्वेष में खोई हुई, जो पर के प्रभाव हैं। आकुलता, भ्रमण।</div>', 'red') +
  '</div>')

ekatva = flow([fbox('Heard (shruta)', 'सुनी हुई', 'red'), fbox('Familiar (parichit)', 'परिचित', 'red'), fbox('Experienced (anubhut)', 'अनुभव की हुई', 'red'),
               arrow('rd'), fbox('Kama, bhoga, bandh: katha known to all', 'काम-भोग-बंध की कथा: सबको ज्ञात', 'red')]) + \
         flow([fbox('Never heard properly, never familiar, never experienced', 'न ठीक से सुनी, न परिचित, न अनुभव की', 'gold'), arrow('rd'),
               fbox('Ekatva-vibhakta soul: not easy to attain', 'एकत्व-विभक्त आत्मा: सुलभ नहीं', 'green')])

nays = table([b('', ''), b('Vyavahar (abhutartha)', 'व्यवहार (अभूतार्थ)'), b('Shuddha-naya / Nishchay (bhutartha)', 'शुद्धनय / निश्चय (भूतार्थ)')],
  [[b('Looks at', 'देखता है'), b('Soul with divisions: stages, qualities, relations with karma', 'भेद सहित आत्मा: अवस्था, गुण, कर्म-संबंध'), b('The soul as it is by itself, one and undivided', 'अपने में ही स्थित, एक और अखंड आत्मा')],
   [b('Use', 'उपयोग'), b('Teaching those at lower stages; the practice of vows', 'निम्न स्तर वालों को उपदेश; व्रतादि का पालन'), b('Understanding what the practice is aiming at; samyagdarshan', 'आचरण का लक्ष्य समझना; सम्यग्दर्शन')],
   [b('Risk', 'जोखिम'), b('Mistaking the stage for the soul', 'अवस्था को आत्मा मान लेना'), b('Claiming the top without having done the practice', 'आचरण किए बिना शिखर का दावा')],
   [b('Image', 'उपमा'), b('The language of the listener (gatha 8)', 'श्रोता की भाषा (गाथा 8)'), b('The meaning that the language carries', 'भाषा जो अर्थ वहन करती है')]])

nine = ('<div class="flow">' + ''.join(fbox(e, h, c) for e, h, c in [
  ('Jiva', 'जीव', 'teal'), ('Ajiva', 'अजीव', 'teal'), ('Punya', 'पुण्य', 'gold'), ('Papa', 'पाप', 'gold'), ('Asrav', 'आस्रव', 'red'),
  ('Bandh', 'बंध', 'red'), ('Samvar', 'संवर', 'green'), ('Nirjara', 'निर्जरा', 'green'), ('Moksha', 'मोक्ष', 'green')]) + '</div>' +
  callout('Gatha 13: the nine padarthas seen by the bhutartha = samyaktva. Seven tattvas (Tattvartha Sutra 1.4) + punya + papa = nine padarthas.', 'गाथा 13: भूतार्थ से देखे गए नौ पदार्थ = सम्यक्त्व। सात तत्त्व (तत्त्वार्थ सूत्र 1.4) + पुण्य + पाप = नौ पदार्थ।', 'info'))

def five_svg():
    import math
    items = [('Abaddha-sprishta', 'अबद्धस्पृष्ट', 'not bound, not touched', 'न बँधी, न स्पर्शित'), ('Ananya', 'अनन्य', 'not another', 'अन्य रूप नहीं'),
             ('Niyat', 'नियत', 'constant', 'स्थिर'), ('Avisesh', 'अविशेष', 'undivided', 'भेद रहित'), ('Asanyukta', 'असंयुक्त', 'not joined', 'असंयुक्त')]
    cx, cy = 340, 190
    s = ['<svg viewBox="0 0 680 380" width="680" role="img" aria-label="Five marks">']
    pos = []
    for i in range(5):
        a = -math.pi / 2 + i * 2 * math.pi / 5
        pos.append((cx + 175 * math.cos(a) * 1.35, cy + 135 * math.sin(a)))
    for x, y in pos:
        s.append(f'<line class="ln" x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}"/>')
    s.append(f'<circle class="nd gold" cx="{cx}" cy="{cy}" r="52"/>')
    s.append(svgtext(cx, cy - 4, 'Shuddha', 'शुद्ध', 't'))
    s.append(svgtext(cx, cy + 14, 'Atma', 'आत्मा', 't'))
    for (x, y), (e, h, e2, h2) in zip(pos, items):
        s.append(f'<rect class="nd acc" x="{x-78:.0f}" y="{y-26:.0f}" width="156" height="52" rx="12"/>')
        s.append(svgtext(f'{x:.0f}', f'{y-3:.0f}', e, h, 't'))
        s.append(svgtext(f'{x:.0f}', f'{y+15:.0f}', e2, h2, 't2'))
    s.append('</svg>')
    return '<div class="svgbox">' + ''.join(s) + '</div>'

ratna = flow([fbox('Vyavahar: the sadhu follows', 'व्यवहार: साधु सेवन करे', 'acc'), arrow('rd'),
              fbox('Samyagdarshan, Samyagjnan, Samyakcharitra', 'सम्यग्दर्शन, सम्यग्ज्ञान, सम्यक्चारित्र', 'gold'), arrow('rd'),
              fbox('Nishchay: the three are the soul itself', 'निश्चय: तीनों आत्मा ही हैं', 'green')])

intro = ('<div class="card">' + bd(
  'The <b>Samaysaar</b> of Acharya Kundkund is the most studied Digambar text on the nature of the soul. It speaks of two ways of looking at everything: <b>Vyavahar</b> (the practical, divided view) and <b>Nishchay</b> (the real, undivided view). These first 16 gathas set up the whole book: what the soul is, why it is hard to see, the use of the two views, and what samyagdarshan is. Read them in order: each gatha builds on the one before.',
  'आचार्य कुन्दकुन्द का <b>समयसार</b> आत्मा के स्वरूप पर सर्वाधिक अध्ययन किया जाने वाला दिगंबर ग्रंथ है। यह हर वस्तु को देखने की दो दृष्टियाँ बताता है: <b>व्यवहार</b> (व्यावहारिक, भेद-दृष्टि) और <b>निश्चय</b> (वास्तविक, अभेद-दृष्टि)। ये प्रथम 16 गाथाएँ पूरे ग्रंथ की भूमिका बनाती हैं: आत्मा क्या है, उसे देखना कठिन क्यों, दोनों दृष्टियों का उपयोग, और सम्यग्दर्शन क्या है। क्रम से पढ़ें: हर गाथा पिछली पर आधारित है।') + '</div>')

PURV = dict(
    path='samaysaar/purvarang-1.html', title=('Samaysaar · Purvarang (gathas 1–16)', 'समयसार · पूर्वरंग (गाथा 1–16)'),
    by=('Acharya Kundkund · the opening: the soul, ekatva and the two views', 'आचार्य कुन्दकुन्द · आरंभ: आत्मा, एकत्व और दो दृष्टियाँ'),
    desc='Samaysaar gathas 1-16: Prakrit original, Hindi and English meaning, and illustrated explanation.',
    crumbs=[('samaysaar/', ('Samaysaar', 'समयसार'))], prev=('./', ('Samaysaar', 'समयसार')), next=None,
    intro=intro, foot=FOOT,
    sections=[
      sec('s1', ('Mangalacharan', 'मंगलाचरण'), ('Mangalacharan and the author’s promise', 'मंगलाचरण और प्रतिज्ञा'), None, [G[1]]),
      sec('s2', ('Svasamay', 'स्वसमय'), ('Svasamay and Parasamay', 'स्वसमय और परसमय'), None, [G[2]], svasamay),
      sec('s3', ('Ekatva', 'एकत्व'), ('Ekatva-vibhakta: why it is rare', 'एकत्व-विभक्त: दुर्लभ क्यों'), None, [G[3], G[4], G[5]], ekatva),
      sec('s4', ('Jnayak', 'ज्ञायक'), ('The knower and the use of vyavahar', 'ज्ञायक और व्यवहार का उपयोग'), None, [G[6], G[7], G[8]]),
      sec('s5', ('Shrutakevali', 'श्रुतकेवली'), ('The Shrutakevali', 'श्रुतकेवली'), None, [G[9], G[10]]),
      sec('s6', ('Two views', 'दो दृष्टियाँ'), ('Bhutartha, abhutartha and samyaktva', 'भूतार्थ, अभूतार्थ और सम्यक्त्व'),
          ('The two views side by side.', 'दोनों दृष्टियाँ साथ-साथ।'), [G[11], G[12], G[13]], nays + nine),
      sec('s7', ('Shuddha-naya', 'शुद्धनय'), ('Shuddha-naya and the Jina-shasana', 'शुद्धनय और जिनशासन'), None, [G[14], G[15]], five_svg()),
      sec('s8', ('Ratnatraya', 'रत्नत्रय'), ('Ratnatraya: practice and essence', 'रत्नत्रय: आचरण और सार'), None, [G[16]], ratna),
    ])

def tile(href, en, hi, sub_en, sub_hi, tag_en, tag_hi, soon=False):
    inner = f'<h3>{b(en, hi)}</h3><p>{b(sub_en, sub_hi)}</p><span class="tag">{b(tag_en, tag_hi)}</span>'
    return f'<div class="tile soon">{inner}</div>' if soon else f'<a class="tile" href="{href}">{inner}</a>'

tiles = '<div class="hub">' + tile('purvarang-1.html', 'Purvarang: gathas 1–16', 'पूर्वरंग: गाथा 1–16', 'Mangalacharan, svasamay, ekatva, nishchay and vyavahar', 'मंगलाचरण, स्वसमय, एकत्व, निश्चय-व्यवहार', 'Open →', 'खोलें →') + \
        tile('', 'Purvarang: gathas 17–38', 'पूर्वरंग: गाथा 17–38', 'The soul and the other: the knower and the known', 'आत्मा और पर: ज्ञायक और ज्ञेय', 'Coming soon', 'जल्द आ रहा है', True) + \
        tile('', 'Jiva-Ajiva adhikar', 'जीव-अजीव अधिकार', 'Gathas 39–68', 'गाथा 39–68', 'Coming soon', 'जल्द आ रहा है', True) + \
        tile('', 'Remaining adhikars', 'शेष अधिकार', 'Karta-karma through Sarvavishuddha-jnana', 'कर्ता-कर्म से सर्वविशुद्ध ज्ञान तक', 'Coming soon', 'जल्द आ रहा है', True) + '</div>'

HUB = dict(
    path='samaysaar/index.html', title=('Samaysaar', 'समयसार'),
    by=('Acharya Kundkund · 415 gathas on the pure nature of the soul', 'आचार्य कुन्दकुन्द · आत्मा के शुद्ध स्वरूप पर 415 गाथाएँ'),
    desc='Samaysaar of Acharya Kundkund: Prakrit gathas with Hindi and English explanation.',
    crumbs=[('samaysaar/', ('Samaysaar', 'समयसार'))], foot=FOOT,
    sections=[dict(id='about', nav=('About', 'परिचय'), title=('About the Samaysaar', 'समयसार परिचय'), intro=None, units=[],
      diagram='<div class="card">' + bd(
        '<b>Samaysaar</b> (Samaya-prabhrit) is the best known work of <b>Acharya Kundkund</b> (traditionally placed around the 1st century CE), written in Prakrit. It has <b>415 gathas</b>. The main commentary is Acharya Amritchandra’s <i>Atmakhyati</i>, with a second commentary by Acharya Jayasena (<i>Tatparyavritti</i>); the Hindi vachanika of Pt. Jaychandra Chhabra made it available to Hindi readers. <b>Each page here gives</b> the Prakrit gatha, its meaning in Hindi and English, explanation, key terms and pictures.',
        '<b>समयसार</b> (समयप्राभृत) <b>आचार्य कुन्दकुन्द</b> की सबसे प्रसिद्ध रचना है (परंपरा से लगभग पहली शताब्दी), प्राकृत भाषा में। इसमें <b>415 गाथाएँ</b> हैं। मुख्य टीका आचार्य अमृतचंद्र की <i>आत्मख्याति</i> है, दूसरी टीका आचार्य जयसेन की <i>तात्पर्यवृत्ति</i>; पं. जयचंद छाबड़ा की हिन्दी वचनिका ने इसे हिन्दी पाठकों तक पहुँचाया। <b>यहाँ हर पृष्ठ पर</b> प्राकृत गाथा, हिन्दी और अंग्रेज़ी अर्थ, व्याख्या, शब्दार्थ और चित्र।') + '</div>'
      + '<h3>' + b('The ten parts of the book', 'ग्रंथ के दस भाग') + '</h3>' + adh + '<h3>' + b('Pages', 'पृष्ठ') + '</h3>' + tiles)])

PAGES = [HUB, PURV]
