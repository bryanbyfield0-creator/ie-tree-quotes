# Site content for Inland Empire Tree Quotes. Used by build.py.
BASE = "https://bryanbyfield0-creator.github.io/ie-tree-quotes"
BRAND = "Inland Empire Tree Quotes"
SHORT_BRAND = "IE Tree Quotes"
EMOJI = "🌳"
EMAIL = "bryanbyfield0@gmail.com"
PHONE = "909-361-0443"
# FormSubmit hashed endpoint (keeps the email address out of the page source). Do not change.
FORM_ACTION = "https://formsubmit.co/f205ca1265cc5630d4c6253a9913f917"
FORM_SUBJECT = "New tree service quote request (IE Tree Quotes)"
# Google Search Console verification token (keep).
GOOGLE_VERIFICATION = "QTObMCEV5W0Joa9lOXm7iWNE78Jmfe1DUmOx7eiV0R4"
INDEXNOW_KEY = "6f1c2b9e8d4a47b3a5e0c7d21f9b3e64"
FACTS_CHECKED = "October 2026"
GUIDES_PUBLISHED = "2026-10-02"
PROVIDER_NOUN = "tree service"
COMPANY_NOUN = "tree company"
SERVICE_TYPE = "Tree service referral"
CTA_TEXT = "Get free tree service quotes"
ORG_DESCRIPTION = "Free referral service that connects Inland Empire property owners with independent local tree service providers for tree removal, trimming, palm trimming, stump grinding, storm cleanup, and brush clearance. Not a tree company."

# (src, w, h, alt, photographer, photographer_url, site, photo_url, license)
PHOTOS = {
 "hero": ("img/arborist-pruning-tree.jpg", 1600, 900, "Arborist in a safety harness pruning a large tree", "Dmytro Glazunov", "https://unsplash.com/@d_glazun0v", "Unsplash", "https://unsplash.com/photos/oqYrgDrs9Xk", "Unsplash License"),
 "palm": ("img/palm-tree-trimming.jpg", 1280, 800, "Tree worker in a harness trimming a tall date palm", "Emilio S\u00e1nchez Hern\u00e1ndez", "https://www.pexels.com/photo/a-palm-tree-in-a-city-16738703/", "Pexels", "https://www.pexels.com/photo/a-palm-tree-in-a-city-16738703/", "Pexels License"),
 "removal": ("img/tree-removal-climber.jpg", 1600, 1091, "Climber on ropes cutting a tall tree down in sections", "Dmytro Glazunov", "https://unsplash.com/@d_glazun0v", "Unsplash", "https://unsplash.com/photos/Bwn-wVh4OfY", "Unsplash License"),
}
SVC_IMG = {"tree-removal":"removal","tree-trimming":"hero","palm-tree-trimming":"palm"}
HOME_SPLIT_IMG = "palm"

SERVICES = [
 ("tree-removal","Tree Removal","Removing dead, dying, leaning, or unwanted trees, including large trees close to houses, fences, and power lines. Pros usually take the tree down in sections, haul the wood away, and can grind the stump if you want."),
 ("tree-trimming","Tree Trimming & Pruning","Crown thinning, raising the canopy, removing dead wood, and clearing branches away from roofs and walls. Good pruning reduces wind damage and keeps trees healthy."),
 ("palm-tree-trimming","Palm Tree Trimming","Removing dead fronds, seed pods, and skirts from Mexican fan palms, California fan palms, queen palms, and date palms. Dead fronds can fall in wind and can be a fire hazard, so many owners trim palms once a year."),
 ("stump-grinding","Stump Grinding","Grinding stumps below grade so you can replant, lay sod, or pave. It's usually much cheaper than full stump excavation."),
 ("emergency-storm","Emergency & Storm Cleanup","Fallen trees and broken limbs after Santa Ana winds or storms, including trees on roofs, cars, or fences. Many tree companies offer same-day or next-day emergency service."),
 ("brush-clearance","Brush Clearance & Defensible Space","Clearing dry brush, dead trees, and overgrowth to create defensible space around homes near the foothills and open land, and handling weed abatement notices."),
]
SVC_SHORT = {
 "tree-removal":"dead, leaning, or unwanted trees taken down in sections and hauled away",
 "tree-trimming":"thinning, deadwood removal, and clearing limbs off roofs and walls",
 "palm-tree-trimming":"dead fronds, seed pods, and skirts removed from tall palms",
 "stump-grinding":"stumps ground below grade so you can replant or pave",
 "emergency-storm":"limbs and trees brought down by wind or storms",
 "brush-clearance":"dry brush and dead vegetation cleared for defensible space",
}
def CITY_SVC_LINE(s, n, c): return SVC_SHORT[s]

# ---- shared sources ----
S_DSPACE=("CAL FIRE: Defensible space","https://www.fire.ca.gov/dspace/")
S_4291=("California Public Resources Code section 4291","https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PRC&sectionNum=4291")
S_BOF=("Board of Forestry: Defensible space zones 0, 1 and 2","https://bof.fire.ca.gov/projects-and-programs/defensible-space-zones-0-1-and-2")
S_FHSZ=("Office of the State Fire Marshal: Fire Hazard Severity Zones","https://osfm.fire.ca.gov/what-we-do/community-wildfire-preparedness-and-mitigation/fire-hazard-severity-zones")
S_SBFHSZ=("San Bernardino County Fire: Fire Hazard Severity Zone map","https://sbcfire.org/fire-hazard-severity-zone-map/")
S_RIVFHSZ=("Riverside 2025 Fire Hazard Severity Zones map viewer","https://experience.arcgis.com/experience/fe0a31d98dc94cf0867d4a4db4427922")
S_NWS=("National Weather Service: Mountain and valley winds (Santa Ana winds)","https://www.weather.gov/safety/wind-mountain-valley")
S_UCIPM=("UC IPM: Palm diseases in the landscape","https://ipm.ucanr.edu/home-and-landscape/palm-diseases-in-the-landscape/")
S_NEST=("CDFW California Outdoors Q&A: nesting birds","https://wildlife.ca.gov/COQA/tag/nesting-birds")
S_RC=("City of Rancho Cucamonga: Tree removal permit checklist (PDF)","https://www.cityofrc.us/sites/default/files/2025-04/CHECKLIST%20-%20Tree%20Removal%20Permit%20UPDATED%2004.2025.pdf")
S_RIVTREE=("City of Riverside: Tree Care Program","https://www.riversideca.gov/publicworks/urban-forestry/tree-care-program")
S_RIVBULKY=("City of Riverside: Bulky items (yard waste bundle rules)","https://www.riversideca.gov/publicworks/trash-recycling/trash/bulky-items")
S_REDL=("City of Redlands: Permit to trim, plant or remove public trees","https://www.redlands.gov/permit-trim-plant-or-remove-public-trees/")
S_WJT=("CDFW: Western Joshua tree frequently asked questions","https://wildlife.ca.gov/Conservation/Environmental-Review/WJT/FAQ")
S_MINOR=("CSLB: License requirement for minor work increases to $1,000 (PDF)","https://www.cslb.ca.gov/Resources/IndustryBulletins/2024/AB%202622%20Implementation.FINAL.pdf")
S_C49=("CSLB: C-49 Tree and Palm classification (PDF)","https://www.cslb.ca.gov/Resources/IndustryBulletins/2023/Tree_and_Palm_Bulletin.pdf")
S_SBSUN=("San Bernardino Sun: The Old and Grand Prix fires of October 2003","https://www.sbsun.com/2018/10/19/photos-the-old-fire-and-grand-prix-fires-destroyed-homes-in-the-inland-area-in-october-of-2003/")
S_DELROSA=("Press-Enterprise: Del Rosa after the Old Fire","https://www.pressenterprise.com/2008/06/10/2008-special-report-del-rosa-put-on-fast-track-to-rebirth/")
S_SBBULKY=("City of San Bernardino: Keep SB Clean (bulky item collection)","https://www.sanbernardino.gov/1099/Keep-SB-Clean")
S_FONBULKY=("City of Fontana: Residential trash services","https://www.fontanaca.gov/2713/Residential-Trash-Services")
S_HESBULKY=("City of Hesperia: Bulky item pick-up program","https://hesperiaca.gov/494/Large-Item-Pick-Up-Program")
S_MVBULKY=("City of Moreno Valley: Bulky item pickup","https://www.moreno-valley.ca.us/resident_services/waste/trash-bulky-item.html")
S_ONTBULKY=("City of Ontario: Bulky item collection","https://www.ontarioca.gov/government/public-works/integrated-waste/bulky-item-collection")

FIRE_P = '''<p>California law (<a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PRC&sectionNum=4291" rel="nofollow">Public Resources Code 4291</a>) requires up to 100 feet of defensible space around buildings in state-mapped fire areas, and many cities apply similar rules through their own weed abatement ordinances. Check whether your address is in a mapped Fire Hazard Severity Zone before fire season.</p>'''

def C_(name, county, intro, local, nearby, faq, sources):
    return dict(name=name, county=county, intro=intro, local=local, nearby=nearby, faq=faq, sources=sources)

CITIES = {
"san-bernardino": C_("San Bernardino","San Bernardino",
 "San Bernardino stretches from older, tree-lined streets near downtown up into foothill neighborhoods such as Verdemont, Del Rosa, and the area around Cal State San Bernardino. The mix means everything from big, mature shade trees over old homes to brushy hillside lots that need clearing before fire season.",
 [("Fire season in the foothill neighborhoods", '''<p>The foothills above San Bernardino have a real fire history. The 2003 Old Fire destroyed hundreds of homes, including many in the Del Rosa area. If your property backs onto the hills, dead trees, dry brush, and palms with thick skirts of dead fronds near the house are the first things to deal with.</p>'''+FIRE_P),
  ("Getting rid of trimmings", '''<p>For small loads, the City of San Bernardino's free bulky-item collection (through Burrtec) lists tree branches among accepted items, with two free collections a year of up to five items each. Big removals are different: most tree services include haul-away in the quote, so ask that it's written in.</p>''')],
 ["Highland","Rialto","Colton","Loma Linda","Redlands"],
 [("Do I need defensible space if I live near the San Bernardino foothills?","If your home is in a state-mapped fire area, Public Resources Code 4291 requires up to 100 feet of defensible space. Check the San Bernardino County Fire hazard map for your address."),
  ("Can the city pick up branches after I trim a tree?","San Bernardino residents get two free bulky-item collections per year (up to five items each) through Burrtec, and tree branches are on the accepted list. Larger jobs are usually hauled by the tree service.")],
 [S_DELROSA,S_SBSUN,S_4291,S_SBFHSZ,S_SBBULKY]),
"fontana": C_("Fontana","San Bernardino",
 "Fontana is one of the windiest places in the Inland Empire. North Fontana neighborhoods near the Cajon Pass corridor, such as Hunter's Ridge, get hit hard when Santa Ana winds blow, and the city still has rows of tall eucalyptus that were planted as windbreaks when the area was farmland.",
 [("Wind and tall trees", '''<p>The National Weather Service says Santa Ana winds are most common from September through May. In Fontana that means broken limbs, split trunks, and fronds blown off tall palms several times a year. Thinning dense canopies and removing deadwood before wind season lowers the risk of a big limb landing on a roof or car.</p>'''),
  ("Old eucalyptus windrows", '''<p>Mature eucalyptus can be very tall, drop heavy limbs, and shed a lot of flammable bark and leaves. If one is leaning, cracked, or hanging over the house, get it looked at by an experienced (ideally certified) arborist before deciding between trimming and removal.</p>'''),
  ("Stumps and trimmings", '''<p>The City of Fontana says its residential trash service includes free curbside removal of large or bulky items, with stumps among the examples, three times per year. That can cover a small stump you dig out yourself, but grinding is usually easier for anything large.</p>''')],
 ["Rialto","Rancho Cucamonga","Ontario","San Bernardino","Upland"],
 [("When is the windiest time of year in Fontana?","The National Weather Service says Santa Ana winds are most common from September through May. Getting trees thinned before late fall is a good idea."),
  ("Will Fontana's trash service take a tree stump?","The city lists stumps among the bulky items Burrtec will pick up curbside for free, three times per year. Call to schedule and confirm size limits.")],
 [S_NWS,S_FONBULKY]),
"rialto": C_("Rialto","San Bernardino",
 "Rialto sits right in the path of the winds that funnel out of the Cajon Pass, between Fontana and San Bernardino. Yards here commonly have mature shade trees, fan palms, and fruit trees, and many of the requests we see are for preventive trimming and cleanup after wind events.",
 [("Wind damage and preventive trimming", '''<p>Santa Ana wind events (most common September through May, according to the National Weather Service) can drop limbs onto roofs, fences, and service drops. Thinning heavy canopies, removing deadwood, and cutting back limbs over the house are the most common preventive jobs in Rialto.</p>'''),
  ("Palms in Rialto yards", '''<p>Tall Mexican fan palms are everywhere here. Left untrimmed, they build up a "skirt" of dead fronds that can fall in wind and burn easily. Ask for dead fronds and seed stalks to be removed. Healthy green fronds should mostly stay, because over-pruning stresses palms.</p>''')],
 ["Fontana","San Bernardino","Colton","Grand Terrace"],
 [("Should I trim my palms before the Santa Ana winds?","Many owners have dead fronds removed before fall, since that's when Santa Ana winds pick up. Check for nesting birds first if you trim in spring or summer.")],
 [S_NWS,S_UCIPM]),
"redlands": C_("Redlands","San Bernardino",
 "Redlands is known for its historic neighborhoods, big old street trees, and leftover citrus groves, from the streets around downtown and the University of Redlands up to Smiley Heights and the south hills. Careful pruning of large, mature trees is a big part of tree work here.",
 [("Street trees need a city permit", '''<p>Redlands requires a Public Tree Encroachment Permit before anyone trims, plants, or removes a tree in a city easement or public right-of-way. If the tree is in your parkway (the strip between the sidewalk and the street), confirm who owns it before you hire anyone. The city's street tree rules call for ISA pruning standards, and removals generally require a replacement tree.</p>'''),
  ("Old citrus and large heritage trees", '''<p>Declining citrus trees, old pepper trees, and big oaks and sycamores are common removal or restoration requests. Large, valuable trees deserve an assessment by an ISA-certified arborist before major cuts.</p>''')],
 ["Loma Linda","Highland","Yucaipa","San Bernardino"],
 [("Do I need a permit to trim a tree in Redlands?","You need a city permit to trim, plant, or remove a tree in a public right-of-way or city easement, such as many parkway trees. Trees fully on private property generally aren't covered by that permit, but check with the city if you're unsure.")],
 [S_REDL]),
"highland": C_("Highland","San Bernardino",
 "Highland runs from established neighborhoods up to East Highlands Ranch and the foothills of the San Bernardino Mountains, and many lots border open land. Dead tree removal, brush clearance, and thinning trees near the house are common requests here, along with routine trimming and stump grinding.",
 [("Brush clearance near open land", FIRE_P+'''<p>On foothill lots, ask providers to quote dead tree removal, limbing up (removing low branches so a ground fire can't climb into the canopy), and chipping or hauling the debris, not just cutting.</p>'''),
  ("Planning around nesting season", '''<p>California law protects active bird nests. CDFW suggests avoiding major tree work during the main nesting months (roughly February through August) where possible, or having the tree checked for active nests first.</p>''')],
 ["San Bernardino","Redlands","Yucaipa","Loma Linda"],
 [("When is the best time to clear brush in Highland?","Before fire season, ideally late winter or spring. Have the area checked for active bird nests if you're clearing during nesting season.")],
 [S_4291,S_SBFHSZ,S_NEST]),
"colton": C_("Colton","San Bernardino",
 "Colton mixes older neighborhoods, commercial lots, and properties along the Santa Ana River and up into Reche Canyon. Common jobs include removing overgrown trees, trimming palms, clearing lots, and grinding stumps left behind by old removals.",
 [("Lots, rentals, and overgrown trees", '''<p>Rental properties and vacant lots often go years without tree work. Overgrown trees touching roofs, palms with heavy dead skirts, and volunteer trees growing against walls or fences are the usual problems. For trees near power lines, contact the utility before anyone climbs.</p>'''),
  ("Reche Canyon hillsides", '''<p>Homes on the Reche Canyon side sit closer to open, brushy hills. Defensible space and dead tree removal matter more there than in the flatland neighborhoods.</p>'''+FIRE_P)],
 ["San Bernardino","Rialto","Loma Linda","Grand Terrace","Riverside"],
 [("Who handles trees touching power lines in Colton?","Don't trim near energized lines yourself. Contact the electric utility that serves your address first. Utilities usually clear lines themselves or tell you how to proceed safely.")],
 [S_4291,S_SBFHSZ]),
"yucaipa": C_("Yucaipa","San Bernardino",
 "Yucaipa's larger lots, oak woodland, and foothill terrain toward Oak Glen and Wildwood Canyon mean bigger trees and more brush than most valley cities. Homeowners commonly want dead or diseased trees removed, oaks and pines pruned, and defensible space cleared around the home.",
 [("Defensible space on big lots", FIRE_P+'''<p>On larger parcels the 100-foot zone can include many trees. The usual approach is to remove dead trees and dry brush, thin dense clumps, and limb up the trees you keep, rather than clear-cutting.</p>'''),
  ("Oaks and pines", '''<p>Native oaks don't respond well to heavy pruning or to soil changes around the roots. Ask for an arborist who works with oaks, and avoid "lion-tailing" (stripping inner branches). Pines stressed by drought are more vulnerable to bark beetles, so dead or dying pines are worth removing promptly.</p>''')],
 ["Redlands","Highland","Loma Linda"],
 [("Do I have to clear brush on my Yucaipa property?","If your parcel is in a state-mapped fire area, state law requires up to 100 feet of defensible space, and local weed abatement rules may also apply. Check the county fire hazard map for your address.")],
 [S_4291,S_DSPACE,S_SBFHSZ]),
"rancho-cucamonga": C_("Rancho Cucamonga","San Bernardino",
 "Rancho Cucamonga runs from the flats along Foothill Boulevard up through Alta Loma and Etiwanda to the base of the San Gabriel Mountains. Wind, old eucalyptus windrows, and foothill fire risk shape most tree work here, and the city has its own heritage tree rules.",
 [("Heritage tree permits", '''<p>Rancho Cucamonga requires a city tree removal permit before you remove, relocate, or top more than 25% of a heritage tree on private property. Qualifying trees are generally defined by height and trunk diameter (20 inches, or 30 inches combined for multi-trunk trees), plus eucalyptus windrows and historically significant trees. Dead trees still need a permit, though the city says there's no fee for those. Ask your provider to confirm whether your tree qualifies before any work starts.</p>'''),
  ("Foothill fire history", '''<p>The 2003 Grand Prix Fire burned homes in Alta Loma and other foothill areas. In the northern foothill neighborhoods closest to the wildland edge, defensible space and removing dead trees near structures should come first.</p>''')],
 ["Upland","Fontana","Ontario","Chino"],
 [("Do I need a permit to remove a tree in Rancho Cucamonga?","For heritage trees, yes, even on private property. That includes topping more than 25% of the canopy. Check the city's tree removal permit checklist or ask the Planning Department."),
  ("Are eucalyptus windrows protected in Rancho Cucamonga?","The city's heritage tree definition includes eucalyptus windrows, so removal generally needs a permit.")],
 [S_RC,S_SBSUN,S_4291]),
"riverside": C_("Riverside","Riverside",
 "Riverside is one of the largest cities in the region, with very different neighborhoods: the historic Wood Streets and downtown, Canyon Crest and Mission Grove near the hills, Orangecrest, La Sierra, and more. It also has deep citrus roots and a large public street-tree canopy.",
 [("Parkway and street trees", '''<p>Many Riverside trees in the parkway belong to the city. Riverside's Tree Care Program lets residents request city tree work, or hire a licensed contractor of their choice under a no-fee street tree permit. Don't let anyone prune or remove a parkway tree until you've confirmed ownership and the permit.</p>'''),
  ("Hauling small loads of trimmings", '''<p>The City of Riverside's bulky-item program takes yard waste and tree trimmings only if tied in bundles no more than 18 inches across and 36 inches long. No large limbs, trunks, or stumps. Anything bigger is a job for the tree service's haul-away.</p>'''),
  ("Hillside neighborhoods", '''<p>Homes near open space such as Sycamore Canyon and the Box Springs Mountains are closer to brush and should keep defensible space in mind.</p>'''+FIRE_P)],
 ["Moreno Valley","Corona","Colton","Grand Terrace"],
 [("Can I hire my own contractor to trim a Riverside street tree?","Yes. Riverside says residents can hire a licensed contractor using a no-fee street tree permit. You can also request work through the city's Tree Care Program."),
  ("Will Riverside's trash service take tree branches?","Only if they're tied in bundles no more than 18 inches in diameter and 36 inches long, through the bulky-item program. Large limbs, trunks, and stumps aren't accepted.")],
 [S_RIVTREE,S_RIVBULKY,S_RIVFHSZ,S_4291]),
"ontario": C_("Ontario","San Bernardino",
 "Ontario combines older neighborhoods around downtown and the tree-lined Euclid Avenue corridor with large newer communities in the south end around Ontario Ranch. Older areas need work on big, mature trees, while newer tracts tend to need routine trimming and palm care before trees outgrow small yards.",
 [("Older trees in established neighborhoods", '''<p>Mature trees in older Ontario neighborhoods can have roots lifting sidewalks and limbs over roofs and power lines. Ask for crown thinning and clearance pruning rather than topping, which leads to weak regrowth.</p>'''),
  ("New communities and HOAs", '''<p>Many newer south Ontario homes are in HOAs with landscaping rules. Check your HOA's guidelines before removing or replacing front-yard trees.</p>'''),
  ("Disposing of trimmings", '''<p>The City of Ontario's bulky-item program accepts bundled or bagged green waste, and single-family homes get up to four appointments a year. That's handy for small DIY trimming jobs.</p>''')],
 ["Upland","Rancho Cucamonga","Chino","Fontana"],
 [("Does Ontario pick up yard trimmings?","Bundled or bagged green waste is accepted in Ontario's bulky-item program, which allows single-family homes up to four appointments per year. Large tree jobs are usually hauled by the tree service.")],
 [S_ONTBULKY]),
"corona": C_("Corona","Riverside",
 "Corona runs from older neighborhoods near downtown's Grand Boulevard circle to hillside areas in south Corona that back onto the Santa Ana Mountains. Common requests range from palm trimming and shade-tree pruning in the flats to dead tree and brush removal on hillside lots.",
 [("Hillside lots near the Santa Ana Mountains", '''<p>Homes on the southern and western edges of Corona sit near brushy open space. Removing dead trees, thinning vegetation near the house, and keeping palms free of dry fronds are priorities.</p>'''+FIRE_P),
  ("Wind through the canyon", '''<p>Santa Ana winds that push toward the coast through the Santa Ana River canyon can be strong in parts of Corona. Thinning top-heavy trees before late fall helps reduce breakage.</p>''')],
 ["Riverside","Chino","Ontario"],
 [("Is my Corona home in a fire hazard zone?","Check the state and Riverside County Fire Hazard Severity Zone maps for your address. Hillside areas near open space are the most likely to be mapped.")],
 [S_RIVFHSZ,S_4291,S_NWS]),
"moreno-valley": C_("Moreno Valley","Riverside",
 "Moreno Valley covers a wide area east of Riverside, from Sunnymead and Moreno Valley Ranch to neighborhoods along the Box Springs Mountains and near Lake Perris. Many homes were built in the last few decades, so trees planted with the houses are now big enough to need regular trimming.",
 [("Trees planted with the houses", '''<p>Fast-growing trees planted in small yards decades ago now crowd roofs, walls, and neighbors. Crown reduction, removing trees that are too close to foundations, and grinding stumps for re-landscaping are common jobs.</p>'''),
  ("Disposing of large branches", '''<p>Moreno Valley's bulky-item program (through Waste Management) accepts oversized yard waste such as tree trunks and large branches, up to two feet in diameter and four feet long. The city says residents can request up to four bulky and/or e-waste pickups per month at no charge.</p>'''),
  ("Box Springs foothills", '''<p>Homes near the Box Springs Mountains and other open hillsides should keep brush and dead trees cleared.</p>'''+FIRE_P)],
 ["Riverside","Corona","Loma Linda"],
 [("Will Moreno Valley pick up tree trunks?","Yes, through the bulky-item program, as long as pieces are no more than two feet in diameter and four feet long. Schedule with Waste Management before your collection day.")],
 [S_MVBULKY,S_RIVFHSZ,S_4291]),
"upland": C_("Upland","San Bernardino",
 "Upland climbs from historic downtown and the Euclid Avenue corridor up to foothill neighborhoods below San Antonio Heights and the San Gabriel Mountains. Large old trees, foothill winds, and fire-season prep shape most tree work here.",
 [("Big trees in established neighborhoods", '''<p>Older Upland neighborhoods have large, mature trees that need skilled pruning, not topping. For big shade trees over houses, ask for a written scope that lists which limbs come out and how cleanup is handled.</p>'''),
  ("North Upland and the foothills", '''<p>North Upland borders the foothills that burned in the 2003 Grand Prix Fire. Defensible space, dead tree removal, and palm frond cleanup near the home are the priorities on these lots.</p>'''+FIRE_P)],
 ["Rancho Cucamonga","Ontario","Chino","Fontana"],
 [("What tree work matters most in north Upland?","Removing dead trees and brush near structures and keeping defensible space. Check the county fire hazard map for your address.")],
 [S_SBSUN,S_4291,S_SBFHSZ]),
"chino": C_("Chino","San Bernardino",
 "Chino still has wide, open parcels from its dairy and farming past alongside newer subdivisions in areas like The Preserve. Larger lots can hold big windbreak trees and old fruit trees, while newer neighborhoods mostly need routine trimming and palm care.",
 [("Large parcels and windbreak trees", '''<p>Rows of tall trees on older agricultural parcels can become hazardous as they age. Before a big removal project, ask for a site visit and a written quote that covers haul-away or chipping, plus stump grinding if you plan to build or landscape.</p>'''),
  ("Newer neighborhoods", '''<p>In newer tracts, the usual requests are trimming trees away from roofs, palm trimming, and replacing trees that were planted too close to the house. Check HOA rules before removing front-yard trees.</p>''')],
 ["Ontario","Upland","Corona","Rancho Cucamonga"],
 [("Do I need to remove old windbreak trees on my Chino property?","Not necessarily. Many can be made safer with deadwood removal and thinning. An arborist can tell you whether a tree is structurally sound.")],
 []),
"hesperia": C_("Hesperia","San Bernardino",
 "Hesperia is in the High Desert, with big lots, cold winters, hot summers, and strong winds. Common tree jobs include removing dead or wind-damaged trees, trimming windbreak trees, clearing dry brush, and dealing with protected Joshua trees.",
 [("Joshua trees are protected", '''<p>Western Joshua trees are protected under California's Western Joshua Tree Conservation Act. Removing or trimming one generally requires a permit from the California Department of Fish and Wildlife. CDFW offers a no-cost hazard permit only for dead trees or for trees that meet specific hazard conditions. Don't hire anyone who offers to quietly take one out.</p>'''),
  ("Wind and dry brush", '''<p>High Desert winds snap brittle limbs and topple shallow-rooted trees. Dead trees and dry brush near structures are both a wind hazard and a fire hazard.</p>'''),
  ("Getting rid of stumps", '''<p>Hesperia's bulky-item program through Advance Disposal accepts tree stumps over 3 inches in diameter. Single-family homes can schedule up to four pickups a year, with a maximum of eight items per year.</p>''')],
 ["Victorville"],
 [("Can I remove a Joshua tree on my Hesperia lot?","Not without checking with CDFW first. Western Joshua trees are protected, and removal or trimming generally needs a permit. Dead or hazardous trees may qualify for a no-cost hazard permit."),
  ("Will Hesperia's trash service take a tree stump?","Advance Disposal's bulky-item program lists tree stumps over 3 inches in diameter as acceptable. Single-family homes can schedule up to four pickups and eight items per year.")],
 [S_WJT,S_HESBULKY]),
"victorville": C_("Victorville","San Bernardino",
 "Victorville spans Old Town along the Mojave River, newer neighborhoods to the west and north, and areas near Spring Valley Lake. As in the rest of the High Desert, wind, drought stress, and protected Joshua trees shape most tree jobs.",
 [("Joshua tree rules", '''<p>Western Joshua trees are protected under state law, and removing or trimming one generally requires a permit from the California Department of Fish and Wildlife. Dead trees or trees that meet hazard conditions may qualify for CDFW's no-cost hazard permit. Check before any work starts.</p>'''),
  ("Drought-stressed and wind-damaged trees", '''<p>Drought-stressed trees drop limbs more easily in the desert wind. Removing deadwood, thinning dense crowns, and taking down dead trees near homes, fences, and driveways are the most common requests.</p>''')],
 ["Hesperia"],
 [("Do I need a permit to trim a Joshua tree in Victorville?","Generally yes. Western Joshua trees are protected, and CDFW handles permits for removal and trimming, with a no-cost hazard permit for qualifying dead or hazardous trees.")],
 [S_WJT]),
"loma-linda": C_("Loma Linda","San Bernardino",
 "Loma Linda is a compact city between San Bernardino, Redlands, and Colton, home to Loma Linda University and its medical center, with hillside neighborhoods rising toward the south hills. Tree work here ranges from pruning mature trees on older lots to clearing brush on hillside properties.",
 [("Hillside homes", '''<p>Homes on the south hills sit closer to open, grassy, and brushy slopes. Keep dry growth and dead trees cleared, and check the county fire hazard map for your address.</p>'''+FIRE_P),
  ("Rentals near the university", '''<p>Many rental properties near the university and medical center need periodic tree work: trimming trees off roofs, removing problem trees, and clearing palms. Landlords often ask for photo-based quotes and work scheduled around tenants.</p>''')],
 ["Redlands","San Bernardino","Colton","Grand Terrace","Highland"],
 [("Can I get a tree quote for a Loma Linda rental without being there?","Many providers can quote from photos and a description, then confirm on site. Mention access details and tenant contact info in your request.")],
 [S_4291,S_SBFHSZ]),
"grand-terrace": C_("Grand Terrace","San Bernardino",
 "Grand Terrace is a small hillside city between Colton and Riverside, below Blue Mountain. Many homes have mature trees on sloped lots, and neighborhoods near Blue Mountain border open space.",
 [("Sloped lots and access", '''<p>Steep yards and tight side access make removals harder and more expensive, because crews may need to rig and lower pieces instead of dropping them. Mention slopes, gates, and access width in your request so quotes are accurate.</p>'''),
  ("Blue Mountain open space", '''<p>Homes next to Blue Mountain should keep dry brush and dead trees cleared.</p>'''+FIRE_P)],
 ["Colton","Riverside","Loma Linda","San Bernardino"],
 [("Why do tree quotes vary so much on Grand Terrace hillside lots?","Access is a big cost factor. Slopes and narrow side yards can mean rigging, more labor, and hand-carrying debris."),],
 [S_4291,S_SBFHSZ]),
}
for k,v in CITIES.items():
    assert v["name"].lower().replace(" ","-")==k, k

def CITY_TITLE(c): return f"Tree Removal & Trimming in {c['name']}, CA | Free Quotes"
def CITY_DESC(c): return f"Free quotes for tree removal, tree trimming, palm trimming, and stump grinding in {c['name']}, CA, plus local tips on permits, wind, and fire season."
def CITY_H1(c): return f"Tree removal & trimming quotes in {c['name']}, CA"
CITY_JOBS_H2 = "Tree services in {city}"
CITY_LINK_TEXT = "{city} tree service"
def CITY_FAQ_COMMON(c):
    return [(f"How much does tree removal cost in {c['name']}?", f"It depends on the tree's size, species, condition, how close it is to buildings or power lines, access, and whether you want haul-away and stump grinding. Comparing two or three written quotes from {c['name']}-area providers is the best way to know. See our <a href=\"../guides/tree-removal-cost-inland-empire.html\">tree removal cost guide</a>.")]

HOME_TITLE = "Tree Removal & Palm Trimming Quotes | Inland Empire | IE Tree Quotes"
HOME_DESC = "Free quotes from local pros for tree removal, trimming, palm trimming, and stump grinding in San Bernardino, Riverside, Fontana, and 15+ Inland Empire cities."
HERO_HTML = '''<h1>Tree removal, trimming & palm tree service quotes in the Inland Empire</h1>
<p>Tell us about your tree job once and we'll connect you with local tree service providers in San Bernardino, Riverside, Fontana, Redlands, and nearby cities. It's free, and you don't have to hire anyone.</p>
<ul class="checks"><li>One short request, free quotes from local providers</li><li>Removals, trimming, palms, stumps, storm cleanup</li><li>No cost and no obligation to hire</li></ul>'''
QUICK_DETAILS_LABEL = "Short details"
QUICK_DETAILS_PLACEHOLDER = "e.g. 2 tall palms need trimming, near the house"
HOME_DISCLOSURE = f"<strong>Plain-English disclosure:</strong> {BRAND} is a referral service, not a tree company. We pass your request to independent local providers who can contact you. We don't do the work, and we can't vouch for any provider's license or insurance, so please verify both before you hire."
HOME_SERVICES_H2 = "Tree services we can help you find"
HOME_HOW_HTML = '''<h2>How it works</h2><ol><li><strong>Describe the job</strong>: what kind of tree, how big, where it is, and how soon you need it done.</li><li><strong>We match you</strong> with independent tree service providers who serve your city.</li><li><strong>Compare quotes</strong> and hire whoever you choose, or nobody at all.</li></ol>'''
TIPS_H2 = "Tips before you hire a tree service"
TIPS_HTML = '''<ul><li>Get at least two or three written quotes that list exactly what's included (haul-away, stump grinding, cleanup).</li><li>In California, tree work over $1,000 (labor and materials) generally requires a CSLB license. Tree companies now use the C-49 Tree and Palm classification. Look up any company at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a> and ask for its certificate of insurance.</li><li>Be careful with door-to-door "storm chasers" who want cash up front.</li><li>Never try to work on trees near power lines yourself. Call your utility.</li><li>Check permit rules for street trees, heritage trees, and Joshua trees. See our <a href="guides/tree-removal-permits-inland-empire.html">permit guide</a>.</li></ul>'''
HOME_FAQ = [("Is this service free?","Yes. Requesting quotes through this site is free for homeowners, and there's no obligation to hire anyone."),
("Are you a tree company?","No. We're a referral service that connects you with independent local tree service providers. We don't do tree work ourselves."),
("How much does tree removal cost in the Inland Empire?","It depends on the tree's size, species, condition, location (near the house, power lines, or a slope), access, and whether you want haul-away and stump grinding. Getting more than one written quote is the best way to know. See our <a href=\"guides/tree-removal-cost-inland-empire.html\">cost factors guide</a>."),
("Do tree companies need a license in California?","Generally yes for jobs of $1,000 or more in labor and materials, or any job that needs a permit or uses helpers. CSLB's tree classification is C-49 Tree and Palm. Look up any company at cslb.ca.gov before hiring, and ask for proof of liability and workers' comp insurance."),
("Do I need a permit to remove a tree?","Sometimes. Street and parkway trees, heritage trees in cities like Rancho Cucamonga, and Joshua trees in the High Desert can all require permits. HOAs may have their own rules. See our <a href=\"guides/tree-removal-permits-inland-empire.html\">permit guide</a>.")]

SERVICES_TITLE = "Tree Services: Removal, Trimming, Palms & Stumps | IE Tree Quotes"
SERVICES_DESC = "Tree removal, tree trimming, palm tree trimming, stump grinding, storm cleanup, and brush clearance quotes from local Inland Empire providers."
SERVICES_H1 = "Tree services in the Inland Empire"
SERVICES_INTRO = "Here are the most common tree jobs homeowners and property managers ask about. Send one request and local providers can quote your job."
SERVICES_NOTE = "Prices depend on tree size, species, access, and hazards. The only reliable number is a written quote from a licensed, insured provider who has seen the job."
SERVICES_EXTRA = '''<h2>Before you book</h2><p>Read our guides on <a href="guides/palm-tree-trimming-season-california.html">when to trim palms</a>, <a href="guides/defensible-space-brush-clearance-inland-empire.html">defensible space and brush clearance</a>, and <a href="guides/tree-removal-permits-inland-empire.html">tree permits in Inland Empire cities</a>.</p>'''
AREAS_TITLE = "Tree Service Areas: San Bernardino & Riverside County | IE Tree Quotes"
AREAS_DESC = "Tree service quotes in 18 Inland Empire cities, including San Bernardino, Riverside, Fontana, Ontario, Corona, Moreno Valley, Redlands, and Rancho Cucamonga."
GUIDES_TITLE = "Tree Care Guides for Inland Empire Homeowners | IE Tree Quotes"
GUIDES_DESC = "Plain-English guides on tree removal costs, palm trimming season, defensible space, Santa Ana wind prep, permits, and hiring a licensed tree service."
GUIDES_INTRO = "Practical, sourced answers to the questions Inland Empire homeowners ask most about their trees."
HOW_TITLE = "How It Works | IE Tree Quotes"
HOW_DESC = "How our free tree service referral works: what we do with your request, who contacts you, and what we are and aren't."
HOW_BODY = f'''<h1>How {BRAND} works</h1>
<p>We're a small, independent referral service based in San Bernardino County. We built this site to make it easier to find someone for tree work without calling a dozen companies.</p>
<ol><li>You fill out the <a href="contact.html">quote request form</a>.</li><li>We review it and share your job details and contact information with one or more independent tree service providers who serve your area.</li><li>Providers contact you directly to schedule an estimate or give a quote.</li><li>You decide who to hire, if anyone. Your agreement is directly with that provider.</li></ol>
<h2>What we are, and what we aren't</h2><ul><li>We're <strong>not</strong> a licensed contractor and we don't do tree work.</li><li>We don't guarantee any provider's work, price, license, or insurance. Please verify a license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a> before hiring.</li><li>We may receive a fee from providers for referrals. It never costs you anything.</li><li>We don't post fake reviews or ratings.</li></ul>
<h2>Tree service companies</h2><p>Do you run a licensed, insured tree service in the Inland Empire and want more local jobs? <a href="contact.html?type=provider">Get in touch</a>.</p>'''
CONTACT_TITLE = "Get Free Tree Service Quotes | IE Tree Quotes"
CONTACT_DESC = "Request free quotes for tree removal, trimming, palm trimming, stump grinding, or storm cleanup anywhere in the Inland Empire."
CONTACT_H1 = "Get free tree service quotes"
CONTACT_NOTE = "Emergency? If a tree is on a power line or there's immediate danger, stay away and call 911 or your electric utility first."
CONTACT_EXTRA_FIELDS = '<label for="timing">How soon?</label><select id="timing" name="timing"><option>Emergency (tree down / hazard)</option><option>Within 1-2 weeks</option><option selected>Within a month</option><option>Just getting prices</option></select>'
CONTACT_DETAILS_LABEL = "Job details (tree type, rough height, number of trees, near house or power lines?)"
THANKS_TEXT = 'We\'ll review it and pass it to local tree service providers who serve your area. They\'ll contact you directly. Please check each provider\'s license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a> before hiring.'
FOOTER_DISCLOSURE = f'<strong>{BRAND}</strong> is a free referral service. We are <strong>not a tree service company</strong>, we don\'t do tree work, and we don\'t hold a contractor\'s license. When you send a request, we pass it to independent local tree service providers who can contact you with quotes. Any provider you hire is solely responsible for its work, licensing, and insurance. Always check a contractor\'s license at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a> and ask for proof of insurance before hiring.'
FOOTER_AREA = "Serving San Bernardino County, western Riverside County, and the High Desert."

SB_ALL = list(CITIES)
GUIDES = [
dict(slug="tree-removal-cost-inland-empire", nav="Tree removal cost", img="removal", all_cities=True,
 title="Tree Removal Cost in the Inland Empire: What Drives the Price",
 h1="How much does tree removal cost in the Inland Empire?",
 desc="What drives tree removal prices in San Bernardino and Riverside counties: size, access, hazards, haul-away, stumps, and permits, plus how to compare quotes.",
 blurb="The factors that make one removal cost far more than another, and how to compare quotes fairly.",
 body='''<p>We don't publish price ranges, because we haven't found a reliable, current source for Inland Empire tree removal prices, and online averages are often national numbers that don't fit local jobs. What we can tell you is what drives the price, so you can describe your job clearly and compare quotes fairly.</p>
<h2>The biggest cost factors</h2><ul>
<li><strong>Size and species.</strong> Taller trees and wider canopies mean more cutting, rigging, and debris. Dense hardwoods and big eucalyptus are heavier to handle than small ornamentals.</li>
<li><strong>What's underneath.</strong> A tree in an open yard can sometimes be felled in one piece. A tree over a roof, pool, fence, or power line has to come down in small, roped sections, which takes more time, crew, and equipment.</li>
<li><strong>Access.</strong> Can a bucket truck or chipper get close? Narrow side yards, slopes (common in Grand Terrace, Loma Linda, and other hillside areas), and backyard-only access add labor.</li>
<li><strong>Condition.</strong> Dead, cracked, or storm-damaged trees can be less predictable and more dangerous to climb.</li>
<li><strong>Power lines.</strong> Work near energized lines requires utility coordination and specially trained crews. Contact your utility first.</li>
<li><strong>Haul-away and cleanup.</strong> Some quotes include chipping and hauling everything, others leave the wood. Get it in writing.</li>
<li><strong>Stump grinding.</strong> Usually priced separately. Ask how deep they grind and whether the grindings are hauled away.</li>
<li><strong>Permits.</strong> Street trees, heritage trees, and Joshua trees can require permits, which add time and sometimes fees. See our <a href="tree-removal-permits-inland-empire.html">permit guide</a>.</li>
<li><strong>Urgency.</strong> Emergency calls after wind events often cost more than scheduled work.</li></ul>
<h2>How to get comparable quotes</h2><ol><li>Send the same photos and description to each provider: the whole tree, the base, and what's around it.</li><li>Ask each quote to list haul-away, stump grinding, cleanup, and permit handling.</li><li>Confirm the company's CSLB license (C-49 Tree and Palm for tree work) and insurance. California requires a license for jobs of $1,000 or more in labor and materials.</li><li>Be cautious of very low cash-only bids, especially after storms.</li></ol>''',
 faq=[("Is stump grinding included in tree removal?","Often not. Many companies price it separately, so ask for it as a line item."),("Do I need a licensed tree service in California?","For jobs of $1,000 or more in labor and materials (or any job that needs a permit or uses helpers), California requires a CSLB license. Tree work falls under the C-49 Tree and Palm classification.")],
 sources=[S_MINOR,S_C49]),
dict(slug="palm-tree-trimming-season-california", nav="Palm trimming season", img="palm", all_cities=True,
 title="Palm Tree Trimming Season in California: When & How Often",
 h1="When is palm tree trimming season in Southern California?",
 desc="When to trim palms in the Inland Empire, how often, why over-trimming hurts, nesting bird rules, and why tools should be cleaned between date palms.",
 blurb="When to trim, how much to take off, nesting birds, and the disease that spreads on dirty saws.",
 body='''<p>Palms are everywhere in the Inland Empire: tall Mexican fan palms (<em>Washingtonia robusta</em>), California fan palms (<em>Washingtonia filifera</em>), queen palms, and Canary Island and other date palms. There's no single legal "palm season," but timing matters for the palm, for wildlife, and for wind and fire safety.</p>
<h2>Best timing</h2><ul>
<li><strong>Before wind season.</strong> The National Weather Service says Santa Ana winds are most common from September through May. Removing dead fronds and heavy seed stalks before fall reduces what can fall on roofs and cars.</li>
<li><strong>Outside the main nesting months when possible.</strong> Palms are favorite nesting spots. California law prohibits needlessly destroying active bird nests, and CDFW suggests avoiding major tree work during roughly February through August where possible, or having the palm checked for nests first.</li>
<li><strong>Before fire season</strong> for palms near structures or open land. Dry frond skirts burn easily and can throw embers.</li></ul>
<p>In practice, many Inland Empire owners schedule palm trimming in late summer or early fall (after a nest check) or in winter.</p>
<h2>How much to cut</h2><p>Remove dead and broken fronds, seed stalks, and fruit. Avoid stripping a palm down to a few fronds at the top (sometimes called a "hurricane cut"). Green fronds feed the palm, and heavy pruning can weaken it over time.</p>
<h2>Clean tools matter for date palms</h2><p>UC IPM warns that Fusarium wilt, a fatal disease of Canary Island date palms, spreads on contaminated pruning tools. It recommends cleaning and disinfecting tools between palms and using hand saws rather than chainsaws on these palms. Ask your provider how they handle it.</p>
<h2>How often?</h2><p>Many fan palms are trimmed once a year. Fast-growing palms or palms near roofs and walkways may need it more often. Ask the provider to look at how much dead growth builds up in a year.</p>''',
 faq=[("Is it illegal to trim palm trees in spring in California?","There's no blanket ban, but it's illegal to needlessly destroy an active bird nest. If you trim during nesting season, have the palm checked first."),("Why do palm trimmers clean their saws?","To avoid spreading diseases like Fusarium wilt, which UC IPM says moves between Canary Island date palms on contaminated tools.")],
 sources=[S_NWS,S_NEST,S_UCIPM]),
dict(slug="defensible-space-brush-clearance-inland-empire", nav="Defensible space", img="removal", all_cities=True,
 title="Defensible Space & Brush Clearance Rules in the Inland Empire",
 h1="Defensible space and brush clearance: what Inland Empire homeowners need to know",
 desc="California's 100-foot defensible space rule (PRC 4291), how zones work, how to check your fire hazard zone in San Bernardino and Riverside counties, and tree tips.",
 blurb="The 100-foot rule, the defensible space zones, and how to check your address on the fire hazard maps.",
 body='''<p>Much of the Inland Empire meets the foothills and open land, and the region has a long fire history, including the 2003 Old and Grand Prix fires in the San Bernardino and Rancho Cucamonga foothills. Here's what the rules say and how tree work fits in.</p>
<h2>The state rule</h2><p>California Public Resources Code 4291 requires people who own or control buildings in state-mapped fire areas to maintain defensible space up to 100 feet from each side of a structure (but not beyond the property line). Local agencies can require more.</p>
<h2>The zones</h2><ul><li><strong>Zone 0 (0–5 feet):</strong> the ember-resistant zone right next to the house. The Board of Forestry has been developing statewide Zone 0 rules. Check the Board's page for current status.</li><li><strong>Zone 1 (5–30 feet):</strong> remove dead plants, leaves, and needles, and keep trees trimmed away from the roof and chimney.</li><li><strong>Zone 2 (30–100 feet):</strong> reduce fuel, space out shrubs and trees, and remove dead material.</li></ul>
<h2>Check your address</h2><p>Use the state Fire Hazard Severity Zone maps, the <a href="https://sbcfire.org/fire-hazard-severity-zone-map/" rel="nofollow">San Bernardino County Fire map</a>, or the <a href="https://experience.arcgis.com/experience/fe0a31d98dc94cf0867d4a4db4427922" rel="nofollow">Riverside 2025 map viewer</a>. Your city or fire department may also send weed abatement notices with local deadlines.</p>
<h2>Tree work that helps</h2><ul><li>Remove dead and dying trees near structures.</li><li>Limb up trees so low branches don't act as a ladder for ground fires.</li><li>Keep branches clear of roofs and chimneys.</li><li>Clean dead frond skirts off palms near the house.</li><li>Chip or haul debris instead of leaving piles.</li></ul><p>Plan big clearing jobs around bird nesting season where you can. See our <a href="palm-tree-trimming-season-california.html">palm trimming guide</a>.</p>''',
 faq=[("How far does defensible space have to go?","Up to 100 feet from each side of a structure, but not past your property line, under PRC 4291. Local rules can require more."),("How do I know if I'm in a fire hazard zone?","Look up your address on the state Fire Hazard Severity Zone maps or the county map viewers linked above.")],
 sources=[S_4291,S_DSPACE,S_BOF,S_FHSZ,S_SBFHSZ,S_RIVFHSZ,S_SBSUN]),
dict(slug="tree-removal-permits-inland-empire", nav="Tree permits", img="hero",
 cities=["rancho-cucamonga","riverside","redlands","hesperia","victorville","ontario","chino","fontana","san-bernardino"],
 title="Do You Need a Permit to Remove a Tree? Inland Empire Rules",
 h1="Do you need a permit to remove or trim a tree in the Inland Empire?",
 desc="Tree permit rules that trip up Inland Empire homeowners: Rancho Cucamonga heritage trees, Riverside and Redlands street trees, HOAs, and protected Joshua trees.",
 blurb="Heritage trees, parkway trees, HOAs, and Joshua trees: when you need permission first.",
 body='''<p>Most trees fully on private property in the Inland Empire can be trimmed without a permit, but there are important exceptions. Getting it wrong can mean fines and replacement requirements, so check first.</p>
<h2>Heritage trees: Rancho Cucamonga</h2><p>Rancho Cucamonga requires a tree removal permit before removing, relocating, or topping more than 25% of a heritage tree, even on private property. Heritage trees generally include large trees by height and trunk diameter (20 inches, or 30 inches combined for multi-trunk trees), eucalyptus windrows, and historically significant trees. Dead trees still need a permit, though there's no fee for those.</p>
<h2>Street and parkway trees: Riverside and Redlands</h2><p>Trees in the parkway or public right-of-way often belong to the city.</p><ul><li><strong>Riverside:</strong> residents can request work through the city's Tree Care Program, or hire a licensed contractor with a no-fee street tree permit.</li><li><strong>Redlands:</strong> trimming, planting, or removing a tree in a city easement or right-of-way requires a Public Tree Encroachment Permit. Removals generally require a replacement tree.</li></ul><p>Other cities have their own street tree rules. Call public works before touching a parkway tree.</p>
<h2>Joshua trees: Hesperia, Victorville, and the High Desert</h2><p>Western Joshua trees are protected under the Western Joshua Tree Conservation Act. Removal or trimming generally needs a CDFW permit. CDFW offers a no-cost hazard permit only for dead trees or trees meeting specific hazard conditions.</p>
<h2>HOAs and rentals</h2><p>Many newer neighborhoods (for example in Ontario Ranch, Chino, and Rancho Cucamonga) have HOA rules on front-yard trees. Renters should get the landlord's written OK.</p>
<h2>Birds</h2><p>Even with no permit required, California law prohibits needlessly destroying active bird nests. Check before cutting in spring and summer.</p>''',
 faq=[("Do I need a permit to cut down a tree on my own property in California?","Usually not, but some cities protect heritage or specimen trees on private property (Rancho Cucamonga is one example), and Joshua trees need a CDFW permit. Check your city's rules first."),("Who is responsible for the tree in my parkway?","Often the city. In Riverside and Redlands, parkway and right-of-way trees fall under city permit rules.")],
 sources=[S_RC,S_RIVTREE,S_REDL,S_WJT,S_NEST]),
dict(slug="santa-ana-winds-tree-safety", nav="Santa Ana wind prep", img="removal",
 cities=["fontana","rialto","rancho-cucamonga","upland","san-bernardino","corona","ontario","hesperia","victorville"],
 title="Santa Ana Winds & Your Trees: Prep and Cleanup Guide",
 h1="Santa Ana winds and your trees: how to prepare and what to do after",
 desc="When Santa Ana winds hit the Inland Empire, warning signs of a risky tree, what to trim before wind season, and what to do safely after a limb falls.",
 blurb="Warning signs of a risky tree, what to trim before wind season, and safe cleanup after a storm.",
 body='''<p>The National Weather Service describes Santa Ana winds as dry, gusty winds pushed through Southern California's mountain passes by high pressure over the desert, most common from September through May. Fontana, Rialto, Rancho Cucamonga, Upland, and other cities near the Cajon Pass and the foothills often see the worst of it.</p>
<h2>Warning signs of a risky tree</h2><ul><li>Dead or hanging branches ("widowmakers")</li><li>Cracks, splits, or a weak V-shaped fork in the trunk</li><li>A new lean, or soil heaving at the base</li><li>Mushrooms, cavities, or decay at the base or roots</li><li>Heavy limbs over the roof, driveway, or power lines</li><li>Palms with thick skirts of dead fronds</li></ul>
<h2>Before wind season</h2><ul><li>Have deadwood removed and dense canopies thinned (not topped).</li><li>Have dead palm fronds and seed stalks removed.</li><li>Have trees near structures inspected, especially large eucalyptus and pines.</li></ul>
<h2>After a limb or tree falls</h2><ol><li>Stay away from downed power lines and anything touching them. Call 911 and your utility.</li><li>Take photos for insurance before cleanup.</li><li>Don't climb or run a chainsaw on a tree under tension. Hire a professional.</li><li>Be wary of door-to-door crews demanding cash up front after storms, and check licenses at cslb.ca.gov.</li></ol>''',
 faq=[("When is Santa Ana wind season?","The National Weather Service says Santa Ana winds are most common from September through May."),("Should I top my tree to protect it from wind?","No. Topping causes weak, fast regrowth that breaks more easily. Thinning and deadwood removal are the standard approach.")],
 sources=[S_NWS]),
dict(slug="hiring-licensed-tree-service-california", nav="Hiring a tree service", img="hero", all_cities=True,
 title="How to Hire a Licensed Tree Service in California (C-49)",
 h1="How to check a tree service's license and insurance in California",
 desc="California's $1,000 minor work limit, the C-49 Tree and Palm license, workers' comp rules for tree services, and a checklist for hiring in the Inland Empire.",
 blurb="The $1,000 license threshold, the C-49 Tree and Palm classification, and a hiring checklist.",
 body='''<p>Tree work is dangerous, and hiring the wrong company can leave you exposed if someone gets hurt or your property is damaged. Here's what California rules say.</p>
<h2>When a license is required</h2><p>Since January 1, 2025, California's "minor work" exemption covers only jobs under $1,000 in combined labor and materials, and only when no building permit is needed and no employees or helpers are used. Splitting a bigger job into smaller contracts doesn't count. Most real tree jobs need a licensed contractor.</p>
<h2>The C-49 Tree and Palm license</h2><p>On January 1, 2024, the Contractors State License Board replaced the old tree service classification with C-49 Tree and Palm. CSLB says tree service licensees must carry workers' compensation insurance (or be self-insured) even if they report having no employees.</p>
<h2>Hiring checklist</h2><ol><li>Look up the license number at <a href="https://www.cslb.ca.gov/" rel="nofollow">cslb.ca.gov</a>. Check that it's active and see the classification.</li><li>Ask for certificates of liability and workers' comp insurance.</li><li>Get a written scope: which trees, what cuts, cleanup, haul-away, stump grinding, and permits.</li><li>Ask whether an ISA-certified arborist will assess large or valuable trees.</li><li>Don't pay large cash deposits up front.</li></ol>''',
 faq=[("What license does a tree service need in California?","CSLB's C-49 Tree and Palm classification, for jobs of $1,000 or more or any job needing a permit or helpers."),("Does a tree service need workers' comp in California?","CSLB says C-49 tree service licensees must carry workers' comp (or be self-insured) even if they claim no employees.")],
 sources=[S_MINOR,S_C49]),
]

CSS = """
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;color:#1f2a1f;line-height:1.6;background:#fff}
a{color:#2e6b30}img{max-width:100%;height:auto}
header{background:#1f4d22;color:#fff}header .wrap{display:flex;align-items:center;justify-content:space-between;gap:1rem;padding-top:.7rem;padding-bottom:.7rem}
.brand{color:#fff;text-decoration:none;font-weight:700;font-size:1.15rem;white-space:nowrap}
nav{display:flex;gap:1.1rem}nav a{color:#e6f2e6;text-decoration:none;font-size:.95rem;white-space:nowrap}nav a:hover{color:#fff;text-decoration:underline}
nav a.nav-cta{background:#f2b33d;color:#1f2a1f;font-weight:700;padding:.3rem .8rem;border-radius:999px}nav a.nav-cta:hover{color:#1f2a1f;text-decoration:none;background:#f7c45e}
.wrap{max-width:1080px;margin:0 auto;padding:1rem 1.25rem}
.hero{position:relative;overflow:hidden;color:#fff;background:#1f4d22}.hero-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 35%;z-index:0}
.hero:before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(100deg,rgba(16,48,20,.9) 0%,rgba(22,64,27,.8) 50%,rgba(22,64,27,.5) 100%)}
.hero .wrap{position:relative;z-index:2;display:grid;grid-template-columns:1.15fr 1fr;gap:2rem;align-items:center;padding-top:2.5rem;padding-bottom:2.5rem}
.hero h1{font-size:2.2rem;line-height:1.2;margin:.25rem 0 .75rem;text-shadow:0 1px 3px rgba(0,0,0,.35)}.hero p{font-size:1.1rem;max-width:620px;text-shadow:0 1px 2px rgba(0,0,0,.35)}
.hero ul.checks{list-style:none;padding:0;margin:1rem 0}.hero ul.checks li{margin:.3rem 0;padding-left:1.6rem;position:relative}.hero ul.checks li:before{content:"\\2713";position:absolute;left:0;color:#f2b33d;font-weight:700}
.quote-card{background:#fff;color:#1f2a1f;border-radius:12px;padding:1.25rem 1.25rem 1rem;box-shadow:0 10px 30px rgba(0,0,0,.28)}
.quote-card h2{margin:0 0 .25rem;font-size:1.3rem}.quote-card p,.quote-card p.small{font-size:.85rem;text-shadow:none;margin:.4rem 0}.quote-card form label{margin-top:.55rem;font-size:.93rem}
.quote-card form textarea{min-height:70px}.quote-card .row{display:grid;grid-template-columns:1fr 1fr;gap:0 .75rem}
.btn{display:inline-block;background:#f2b33d;color:#1f2a1f;padding:.8rem 1.4rem;border-radius:6px;font-weight:700;text-decoration:none;border:0;cursor:pointer;font-size:1rem}.btn:hover{background:#f7c45e}
.btn-block{display:block;width:100%;text-align:center}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem}.card{border:1px solid #dfe8df;border-radius:8px;padding:1rem;background:#fafdf9}
.card h3{margin-top:0}.note{background:#fff8e6;border-left:4px solid #f2b33d;padding:.8rem 1rem;border-radius:4px}
.split{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;align-items:center}.photo{display:block;width:100%;border-radius:10px;object-fit:cover}
.split .photo{aspect-ratio:3/2}.svc{display:grid;grid-template-columns:260px 1fr;gap:1.25rem;align-items:start;margin:1.5rem 0}.svc .photo{aspect-ratio:4/3;margin-top:1.2rem}.svc h2{margin-top:.6rem}
form label{display:block;font-weight:600;margin-top:.8rem}form input,form select,form textarea{width:100%;padding:.6rem;border:1px solid #b9c9b9;border-radius:6px;font:inherit;background:#fff;color:inherit}
form label.consent{font-weight:400;font-size:.88rem;display:flex;gap:.5rem;align-items:flex-start}form label.consent input{width:auto;margin-top:.3rem;flex:none}
form textarea{min-height:110px}.small{font-size:.85rem;color:#4a5a4a}footer{background:#f0f5ef;margin-top:2rem;font-size:.9rem}footer .credits{font-size:.78rem;color:#5a6a5a}
.crumbs{font-size:.85rem;margin:.25rem 0 .5rem;color:#4a5a4a}.crumbs a{color:inherit}
ul.sources{font-size:.85rem;padding-left:1.2rem}h2.h3{font-size:1.15rem;margin-top:0}.card h3 a,.card h2 a{text-decoration:none}
.guide>.photo{aspect-ratio:16/9;max-height:440px;margin:1rem 0}
ul.cities{columns:2;padding-left:1.2rem}.mobile-cta{display:none}
@media(max-width:820px){.hero .wrap{grid-template-columns:1fr;gap:1.25rem;padding-top:1.5rem;padding-bottom:1.75rem}.split{grid-template-columns:1fr}}
@media(max-width:640px){
header .wrap{flex-direction:column;align-items:stretch;gap:.35rem;padding-top:.6rem;padding-bottom:0}.brand{font-size:1.05rem}
nav{overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;gap:1rem;padding:.25rem 0 .6rem;margin:0 -1.25rem;padding-left:1.25rem;padding-right:1.25rem}nav::-webkit-scrollbar{display:none}nav a{font-size:.92rem}nav a.nav-cta{display:none}
.hero h1{font-size:1.6rem}.hero p{font-size:1rem}.hero ul.checks{display:none}.quote-card{padding:1rem}.quote-card .row{grid-template-columns:1fr}
.svc{grid-template-columns:1fr;gap:0}.svc .photo{margin-top:.5rem}
body.has-mcta{padding-bottom:76px}.mobile-cta{display:block;position:fixed;left:0;right:0;bottom:0;z-index:50;padding:.6rem 1rem calc(.6rem + env(safe-area-inset-bottom));background:rgba(255,255,255,.96);box-shadow:0 -2px 12px rgba(0,0,0,.15)}
.mobile-cta a{display:block;text-align:center;background:#f2b33d;color:#1f2a1f;font-weight:700;text-decoration:none;padding:.75rem;border-radius:8px;font-size:1.05rem}
}
"""


# Cross-link to the sister lead site (footer)
SISTER_SITE = 'Need junk or yard debris hauled away too? Get free quotes at <a href="https://bryanbyfield0-creator.github.io/ie-junk-quotes/">IE Junk Quotes</a>.'
