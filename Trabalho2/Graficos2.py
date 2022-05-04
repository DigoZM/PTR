from statistics import mean
import matplotlib.pyplot as plt
import numpy as np


Execution_times_listen_request = [0.0010046958923339844]
Execution_times_manage_flight_zones = [0.1340034008026123,0.10799527168273926,0.07500600814819336,0.0010075569152832031,0.0009968280792236328,0.0009984970092773438,0.0009899139404296875,0.0010066032409667969,0.001001119613647461,0.002019166946411133,0.0010132789611816406,0.0009927749633789062,0.0010030269622802734,0.0010046958923339844,0.0009982585906982422,0.0009815692901611328,0.0010356903076171875,0.000993490219116211,0.0009999275207519531,0.0009963512420654297,0.0009920597076416016,0.0009965896606445312,0.0010023117065429688,0.0009992122650146484,0.0009996891021728516,0.0010058879852294922,0.0010020732879638672,0.0010006427764892578,0.0009698867797851562,0.001005411148071289,0.0010104179382324219,0.0010023117065429688,0.0009949207305908203,0.0010135173797607422,0.0010094642639160156,0.0010030269622802734,0.0010013580322265625,0.0010001659393310547,0.0010030269622802734,0.0010004043579101562,0.0009694099426269531,0.0010075569152832031,0.0010101795196533203,0.0009891986846923828,0.0010008811950683594,0.0020165443420410156,0.001003265380859375,0.0009732246398925781,0.0009679794311523438,0.0009658336639404297,0.0010056495666503906,0.000978231430053711,0.0010037422180175781,0.0009579658508300781,0.0010080337524414062,0.0009944438934326172,0.0010056495666503906,0.0010046958923339844,0.000997304916381836,0.0009925365447998047,0.0009989738464355469,0.0010085105895996094,0.0010113716125488281,0.001003265380859375,0.001008749008178711,0.000997781753540039,0.001004934310913086,0.0010061264038085938,0.001004934310913086,0.0009920597076416016,0.0010035037994384766,0.0010035037994384766,0.0009992122650146484,0.0010004043579101562,0.0009970664978027344,0.0010006427764892578,0.00099945068359375,0.0010039806365966797,0.0010027885437011719,0.0010013580322265625,0.0009984970092773438,0.0010023117065429688,0.0010027885437011719,0.0010013580322265625,0.0009968280792236328,0.0010001659393310547,0.0009963512420654297,0.0009968280792236328,0.0009968280792236328,0.0009984970092773438,0.0009992122650146484,0.0010008811950683594,0.0010001659393310547,0.0009996891021728516,0.0010061264038085938,0.0010020732879638672,0.0009818077087402344,0.0010094642639160156,0.0009996891021728516,0.0010058879852294922,0.0010035037994384766,0.0010075569152832031,0.0010035037994384766,0.0010008811950683594,0.0009641647338867188,0.0009951591491699219,0.0010004043579101562,0.0009958744049072266,0.0009620189666748047,0.0010023117065429688,0.0009958744049072266,0.0010027885437011719,0.0009987354278564453,0.00099945068359375,0.0009610652923583984,0.0009636878967285156,0.0009953975677490234,0.0010001659393310547,0.0009968280792236328,0.0009560585021972656,0.0009751319885253906,0.0009446144104003906,0.0010035037994384766,0.0010099411010742188,0.0010023117065429688,0.0010025501251220703,0.0009999275207519531,0.0010025501251220703,0.0009996891021728516,0.0009930133819580078,0.001004934310913086,0.0009961128234863281,0.0020155906677246094,0.0010061264038085938,0.0009996891021728516,0.0009989738464355469,0.000993967056274414,0.0009908676147460938,0.0010001659393310547,0.0009984970092773438,0.0010039806365966797,0.0010020732879638672,0.003008127212524414,0.0010013580322265625,0.0009958744049072266,0.0009996891021728516,0.000995635986328125,0.0009987354278564453,0.001001119613647461,0.0009667873382568359,0.0010030269622802734,0.0009677410125732422,0.0009908676147460938,0.0010001659393310547,0.0009982585906982422,0.0009667873382568359,0.0009980201721191406,0.0010004043579101562,0.001003265380859375,0.0009908676147460938]
Execution_times_wait_list = [0.05499601364135742,0.029000520706176758,0.001007080078125,0.0010027885437011719,0.0009968280792236328,0.0009992122650146484,0.0009663105010986328,0.0009691715240478516,0.001001596450805664,0.0010046958923339844,0.0010180473327636719,0.0010044574737548828,0.0009710788726806641,0.0009565353393554688,0.0009658336639404297,0.0010013580322265625,0.0009558200836181641,0.001001119613647461,0.0010008811950683594,0.001001596450805664,0.0010013580322265625,0.0009682178497314453,0.0009663105010986328,0.0009961128234863281,0.0009965896606445312,0.0009665489196777344,0.000995635986328125,0.0010116100311279297,0.0010018348693847656,0.0009646415710449219,0.0010008811950683594,0.0009922981262207031,0.0009765625,0.0009481906890869141,0.00099945068359375,0.0009503364562988281,0.008994817733764648,0.001001119613647461,0.0009968280792236328,0.001003265380859375,0.0010075569152832031,0.0009968280792236328,0.0009706020355224609,0.00900411605834961,0.001010894775390625,0.0010039806365966797,0.0009996891021728516,0.0009517669677734375,0.0009679794311523438,0.0009999275207519531,0.0009992122650146484,0.0009582042694091797,0.001997232437133789,0.0009992122650146484,0.0010020732879638672,0.0009839534759521484,0.001010894775390625,0.0010008811950683594,0.001001119613647461,0.0010008811950683594,0.0010020732879638672,0.0009980201721191406,0.0010027885437011719,0.0009713172912597656,0.001001119613647461,0.0010039806365966797,0.0009992122650146484,0.0010018348693847656,0.0009987354278564453,0.0019986629486083984,0.0010237693786621094,0.0010020732879638672,0.0009646415710449219,0.0010094642639160156,0.0009644031524658203,0.0009510517120361328,0.00099945068359375,0.0009672641754150391,0.0009582042694091797,0.0009765625,0.0009999275207519531,0.0009644031524658203,0.0010027885437011719,0.0010001659393310547,0.0009658336639404297,0.0009694099426269531,0.0009489059448242188,0.0009677410125732422,0.0009560585021972656,0.0009658336639404297,0.0009655952453613281,0.0009684562683105469,0.000997781753540039,0.0009663105010986328,0.00096893310546875,0.0009679794311523438,0.0019593238830566406,0.0010020732879638672,0.0009927749633789062,0.0010023117065429688,0.0009989738464355469,0.0009989738464355469,0.0009930133819580078,0.001003265380859375,0.0010025501251220703,0.0010080337524414062,0.0010023117065429688,0.0010027885437011719,0.0009987354278564453,0.0009970664978027344,0.001997709274291992,0.001001119613647461,0.0009608268737792969,0.0009665489196777344,0.0010020732879638672,0.0010025501251220703,0.0010027885437011719,0.0009992122650146484,0.0009567737579345703,0.0010025501251220703,0.0009624958038330078,0.0010037422180175781,0.0009951591491699219,0.0010008811950683594,0.0009586811065673828,0.00099945068359375,0.0009946823120117188,0.0009920597076416016,0.0010004043579101562,0.0009853839874267578,0.0010080337524414062]
Execution_times_fly = [0.009000778198242188,0.0010061264038085938,0.0010013580322265625,0.0009984970092773438,0.0009717941284179688,0.0010018348693847656,0.0010020732879638672,0.001998424530029297,0.0019960403442382812,0.0009951591491699219,0.0019593238830566406,0.001993417739868164,0.0010008811950683594,0.0010018348693847656,0.0019626617431640625,0.0020062923431396484,0.0019919872283935547,0.002010345458984375,0.0020012855529785156,0.0020055770874023438,0.0009753704071044922,0.02001023292541504,0.0009975433349609375,0.0009648799896240234,0.0009696483612060547,0.0009996891021728516,0.0010004043579101562,0.0020132064819335938,0.001997232437133789,0.0020003318786621094,0.0009970664978027344,0.0020020008087158203,0.0009608268737792969,0.001001119613647461,0.0019986629486083984,0.0009999275207519531,0.0009937286376953125,0.0009999275207519531,0.0009553432464599609,0.0009555816650390625,0.0009987354278564453,0.0019979476928710938,0.0010001659393310547,0.0009684562683105469,0.0010027885437011719,0.0019998550415039062,0.0010056495666503906,0.0010013580322265625,0.0010008811950683594,0.001001119613647461,0.0010042190551757812,0.0020029544830322266,0.0009586811065673828,0.0010025501251220703,0.0010046958923339844,0.0010006427764892578,0.0010037422180175781,0.0020020008087158203,0.001961946487426758,0.0009682178497314453,0.0010020732879638672,0.0020051002502441406,0.001970052719116211,0.0010030269622802734,0.0009982585906982422,0.001003265380859375,0.002000093460083008,0.0009748935699462891,0.0009636878967285156,0.0009970664978027344,0.0010044574737548828,0.0010020732879638672,0.0010037422180175781,0.0009682178497314453,0.0010006427764892578,0.0009593963623046875,0.0010004043579101562,0.0009884834289550781,0.0020101070404052734,0.0009970664978027344,0.002012014389038086,0.0009961128234863281,0.0010042190551757812,0.001001596450805664,0.0010058879852294922,0.0009551048278808594,0.000997304916381836,0.0009465217590332031,0.0009684562683105469,0.001966714859008789,0.0010271072387695312,0.0019850730895996094,0.002034902572631836,0.0010008811950683594,0.0020041465759277344,0.0009577274322509766,0.0009634494781494141,0.0009999275207519531,0.0010039806365966797,0.0010025501251220703,0.0009987354278564453,0.001001119613647461,0.0009658336639404297,0.002000570297241211,0.0009982585906982422,0.001001596450805664,0.002000093460083008,0.0009632110595703125,0.0010027885437011719,0.0010020732879638672,0.000957489013671875,0.0010008811950683594,0.0019958019256591797,0.0010042190551757812,0.00099945068359375,0.001993417739868164,0.0009570121765136719,0.002001523971557617,0.0019571781158447266,0.0009975433349609375,0.0019648075103759766,0.000972747802734375,0.0009958744049072266,0.0009660720825195312,0.0009984970092773438,0.0010039806365966797,0.0010025501251220703,0.0070078372955322266,0.0009984970092773438,0.002001523971557617,0.0009982585906982422,0.001998424530029297,0.000997304916381836,0.0009965896606445312,0.001995086669921875,0.000997781753540039,0.0010027885437011719,0.0010018348693847656,0.001960277557373047,0.0009746551513671875,0.0010030269622802734,0.0009701251983642578,0.0019805431365966797,0.0009663105010986328,0.000978231430053711,0.0020046234130859375,0.0019996166229248047,0.0009987354278564453,0.0009696483612060547,0.000965118408203125,0.0009663105010986328,0.001016855239868164,0.001978158950805664,0.004996538162231445,0.0019991397857666016,0.0010023117065429688,0.0009722709655761719,0.0009691715240478516,0.002001523971557617,0.002003192901611328,0.0010020732879638672,0.0009987354278564453,0.001956939697265625,0.0009548664093017578,0.002003192901611328,0.0009615421295166016,0.0010039806365966797,0.0019922256469726562,0.002003908157348633,0.0019948482513427734,0.0009760856628417969,0.0009970664978027344,0.0010051727294921875,0.001955747604370117,0.0009546279907226562,0.0019991397857666016,0.0019571781158447266,0.0019989013671875,0.0010004043579101562,0.0019974708557128906,0.0020034313201904297,0.0020020008087158203,0.0009667873382568359,0.001965761184692383,0.0010006427764892578,0.0019991397857666016,0.001001596450805664,0.001001119613647461,0.0010004043579101562,0.0009970664978027344,0.0009996891021728516,0.0010008811950683594,0.0009653568267822266,0.001990795135498047,0.00196075439453125,0.0019745826721191406,0.0020110607147216797,0.0009980201721191406,0.0020084381103515625,0.001997709274291992,0.0009672641754150391,0.0010023117065429688,0.002002239227294922,0.0009975433349609375,0.0010006427764892578,0.0029947757720947266,0.002000093460083008,0.0009653568267822266,0.0009655952453613281,0.0009996891021728516,0.001966714859008789,0.0009777545928955078,0.0010056495666503906,0.03099966049194336,0.0009675025939941406,0.0020089149475097656,0.0019936561584472656,0.0010018348693847656,0.0009641647338867188,0.0009801387786865234,0.0010025501251220703,0.0009746551513671875,0.0009677410125732422,0.0009999275207519531,0.004019498825073242,0.0020122528076171875,0.0009667873382568359,0.0019779205322265625,0.0010058879852294922,0.0020020008087158203,0.001001596450805664,0.0009772777557373047,0.0009586811065673828,0.0009691715240478516,0.0009634494781494141,0.0009982585906982422,0.002000570297241211,0.001994609832763672,0.0020003318786621094,0.0020110607147216797,0.0009531974792480469,0.0009646415710449219,0.0009996891021728516,0.000997781753540039,0.001004934310913086,0.0019769668579101562,0.0019958019256591797,0.0010018348693847656,0.0009999275207519531,0.0009970664978027344,0.0019392967224121094,0.0009670257568359375,0.0010006427764892578,0.0010030269622802734,0.0009684562683105469,0.0010027885437011719,0.0010004043579101562,0.0009791851043701172,0.000982522964477539,0.0010004043579101562,0.0010044574737548828,0.0019834041595458984,0.0020041465759277344,0.0010006427764892578,0.0010013580322265625,0.0009696483612060547,0.0010039806365966797,0.0009658336639404297,0.001005411148071289,0.0010030269622802734,0.0020143985748291016,0.0009710788726806641,0.0010025501251220703,0.007994413375854492,0.0010001659393310547,0.0019762516021728516,0.0019998550415039062,0.0009660720825195312,0.002009153366088867,0.0009686946868896484,0.001001119613647461,0.0010042190551757812,0.0010001659393310547,0.0009660720825195312,0.0010030269622802734,0.0009920597076416016,0.0019996166229248047,0.002002716064453125,0.0010018348693847656,0.0009665489196777344,0.0010020732879638672,0.0019638538360595703,0.0009698867797851562,0.0009579658508300781,0.002016782760620117,0.0010013580322265625,0.0020041465759277344,0.0009677410125732422,0.001967906951904297,0.0010006427764892578,0.0010004043579101562,0.001001119613647461,0.001001596450805664,0.0020003318786621094,0.0009663105010986328,0.0009913444519042969,0.0010006427764892578,0.001001119613647461,0.0009980201721191406,0.0010039806365966797,0.0009691715240478516,0.0009684562683105469,0.0010030269622802734,0.0009586811065673828,0.0009646415710449219,0.0009644031524658203,0.0010020732879638672,0.001979827880859375,0.002000093460083008,0.0009679794311523438,0.0010056495666503906,0.0010008811950683594,0.0010030269622802734,0.0010025501251220703,0.001001119613647461,0.0030498504638671875,0.0009589195251464844,0.0020248889923095703,0.0009682178497314453,0.0010013580322265625,0.0010018348693847656,0.0009639263153076172,0.0009658336639404297,0.001997232437133789,0.0009703636169433594,0.0019648075103759766,0.001001119613647461,0.002002239227294922,0.0009615421295166016,0.0009675025939941406,0.0010023117065429688,0.002009868621826172,0.002000093460083008,0.0009963512420654297,0.003990650177001953]
Execution_times_emergency_button = [0.0010085105895996094,0.0010037422180175781,0.0009932518005371094,0.0010042190551757812,0.0010063648223876953,0.0010042190551757812,0.0010077953338623047,0.0009996891021728516,0.0009958744049072266,0.0010004043579101562,0.0010020732879638672,0.0010082721710205078,0.001001596450805664,0.0009996891021728516,0.0009992122650146484,0.0010035037994384766,0.0009868144989013672,0.0010008811950683594,0.0009951591491699219,0.0010035037994384766,0.0009999275207519531,0.0009963512420654297,0.0009992122650146484,0.0009996891021728516,0.0009927749633789062,0.0009887218475341797,0.0009989738464355469,0.0009965896606445312,0.0010004043579101562,0.0009953975677490234,0.0010149478912353516,0.0010073184967041016,0.0010116100311279297,0.0009992122650146484,0.0009992122650146484,0.0009982585906982422,0.001001119613647461,0.0009944438934326172,0.0019872188568115234,0.0010085105895996094,0.0010006427764892578,0.0009772777557373047,6.437301635742188e-05,6.127357482910156e-05,0.0009944438934326172,0.0009667873382568359,0.0009925365447998047,0.001001596450805664,0.0010228157043457031,0.0010156631469726562,0.001012563705444336,0.0009975433349609375,0.0009946823120117188,0.0009968280792236328,0.0009965896606445312,0.00096893310546875,0.0009906291961669922,0.0009944438934326172,0.0009987354278564453,0.0010101795196533203,0.0009958744049072266,0.0009930133819580078,0.0009970664978027344,0.000997781753540039,0.004000425338745117,0.0009565353393554688,0.0010023117065429688,0.0010209083557128906,0.0010080337524414062,0.0019843578338623047,0.0010139942169189453,0.0010001659393310547,0.0029747486114501953,0.0009829998016357422,0.0009944438934326172,0.005971670150756836,0.001007080078125,0.0010018348693847656,0.001003265380859375,0.0009829998016357422,0.002012968063354492,0.002002239227294922,0.0010044574737548828]

listas = [Execution_times_listen_request,Execution_times_manage_flight_zones,Execution_times_wait_list,Execution_times_fly,Execution_times_emergency_button]

max_values= [max(Execution_times_listen_request),max(Execution_times_manage_flight_zones),max(Execution_times_wait_list),max(Execution_times_fly),max(Execution_times_emergency_button)]


medias = [mean(Execution_times_listen_request),mean(Execution_times_manage_flight_zones),mean(Execution_times_wait_list),mean(Execution_times_fly),mean(Execution_times_emergency_button)]
labels = ['LR','MFZ','W','F','B']



fig, ((ax0,ax1),(ax2,ax3),(ax4,ax5)) = plt.subplots( nrows=3,ncols=2)

for i in range(len(listas)):
    print(i,":Tam: ",len(listas[i]))


ax0.hist(Execution_times_listen_request,bins=30)
ax1.hist(Execution_times_manage_flight_zones,bins=15)
ax2.hist(Execution_times_wait_list,bins=6)
ax3.hist(Execution_times_fly,bins=10)
ax4.hist(Execution_times_emergency_button,bins=50)
ax5.hist(0,bins=1)
plt.show()




#for i in range(len(labels)):
#    plt.figure()
#    plt.plot(range(len(listas[i])), listas[i],'r--')
#    plt.title(labels[i])
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    #plt.axis([40, 160, 0, 0.03])
#    plt.grid(True)
#    plt.show()

