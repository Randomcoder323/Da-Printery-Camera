# Da-Printery-Camera


# March 19 4:57 : Found Items on Aliepxress and made a visual diagram
I started by brainstroming idea for this project. I started by tring to figure out what ports I could use on my printer, I figured out that only the ams 4 pin port if free. I then knew that the only way was to connect it to my computer, which I'm fine with. I found a usb camera on alipress, for only about 10 dollars. I added that to the bom. I then found a micro controller, and esp32 with wifi and bluetooth. For my trigger sensor I'm using a limit switch to detect when the printer moves out the way. I then went onto canva, found image of the stuff I'm gonna use, and made a really helpful visual diagram. I choose a curved 21 mm switch for easier reach from the printer

<img width="1034" height="579" alt="image" src="https://github.com/user-attachments/assets/6b75d76c-203c-4e6f-8f66-4db1d3e58c83" />
<img width="543" height="464" alt="image" src="https://github.com/user-attachments/assets/96722aab-d295-41be-bff6-48c94802bf8b" />
<img width="454" height="430" alt="image" src="https://github.com/user-attachments/assets/1b3f59e1-9613-4896-aa9d-90467a3b2201" />
<img width="1064" height="456" alt="image" src="https://github.com/user-attachments/assets/12dc371a-6610-4059-8944-9f40f6f7c8cb" />


**Total time spent: 0.7**

# March 19 5:38 : Limit Switch mount

Brfore starting anything I tried to find dimension online for the a1 mini and my limti switch I found some info online, but this was the most helpful! I then found some model online for the poop shot and got the neaurment for that from there. I started by building the outside diameted, with a circled side and the oval kidn shape for the poop shute holder. <img width="654" height="268" alt="image" src="https://github.com/user-attachments/assets/c740c29f-b241-4cd4-ac1d-5de583f540c7" /> I then started the bottom side of the mount and made the rectangular bottom and the plate at the bottom. <img width="614" height="398" alt="image" src="https://github.com/user-attachments/assets/9477dd85-225b-4d94-a1ca-fdb1838c8494" />. I then extruded everything and matche dthe heights. I then also made holder for the switch to be mounted with some screws. I added tolarances and a chamfer!


<img width="456" height="337" alt="image" src="https://github.com/user-attachments/assets/a5ac22ef-47d3-492d-af2e-b7d9a7079eaf" />
<img width="822" height="533" alt="image" src="https://github.com/user-attachments/assets/37effa94-2d0f-4e5d-9077-8cdc9acb13ab" />
<img width="654" height="576" alt="image" src="https://github.com/user-attachments/assets/8d14dfce-fb46-4611-ab64-32a1834eb3fc" />
<img width="627" height="709" alt="image" src="https://github.com/user-attachments/assets/d1b075d0-2443-47bc-a45d-d248a70c30d0" />

<img width="1005" height="681" alt="image" src="https://github.com/user-attachments/assets/9b070b50-c5cc-4a47-aa3f-c57f62d7af14" />

<img width="892" height="732" alt="image" src="https://github.com/user-attachments/assets/9c0f61a9-324a-4bc7-baf4-a364e267f041" />



**Total time spent: 0.67**


# March 19 6:12 : Assembly in onshape

I started by exporting my parts and putting them into onshape. I took the limit siwtch name off of aliexpress and found a model online. I then found a really good a1 mini model online on reddit. I copied the onshape asssembly and added my part to the side. It was really dificult trying to the the mate connector to work but I got it. I then imported the limit switch, however I found no way to merge the bodies in assembly. I then had to mate connect all the parts which took a bit. I had to find the rigt way to mate connect it to the printer, but I then figured out that I could amte connect it then delete the connect and move it reigularly slight to manually adjust it. I will add the electronic box next journal!

<img width="475" height="509" alt="image" src="https://github.com/user-attachments/assets/95ba0383-e6d1-4ba0-bbfc-8ca00a9690ef" />

<img width="1005" height="768" alt="image" src="https://github.com/user-attachments/assets/2d26e9c0-a34d-4eb7-8a58-dc2bfe478444" />


**Total time spent: 0.5**

# March 20 7:46 AM : BOM and es 32 box+assembly.
I started by taking all thr components I needed and found the link in aliexpress. I put in the prices, and doubled checked that they are 1.what I needed, and 2. that they are the cheapest possible. I then cleaned it up so any one can follow it. I then found an esp32 model online, so I can get the mesurments and make sure it fits. I made the box around 1mm bigger, and made a lid with some good tolerances. I brought it into onshape and put the esp32 inside it, I really like how it looks. I will either add holes to the top or other side, so the wire has somewhere to go!


<img width="1201" height="783" alt="image" src="https://github.com/user-attachments/assets/48e8871f-fa8e-49b2-bac2-cd43aa3bb294" />

<img width="855" height="604" alt="image" src="https://github.com/user-attachments/assets/483e2aac-fe59-4d85-b08e-5b57a559b699" />

<img width="1003" height="678" alt="image" src="https://github.com/user-attachments/assets/3ee17111-1524-4c82-9a91-8030b99ca5d5" />
<img width="1064" height="820" alt="image" src="https://github.com/user-attachments/assets/3a87bf17-c281-46e3-8f62-62d496b50efe" />
<img width="982" height="745" alt="image" src="https://github.com/user-attachments/assets/553ac8fc-90db-4a10-873c-b9c05159a3e0" />
<img width="847" height="267" alt="image" src="https://github.com/user-attachments/assets/66bc88fc-456e-441c-ba18-146e34f034b9" />

**Total time spent: 0.75**

# March 20 8:42pm : Code, wiring, and read.md

I started by making a quick demo wiring diagram on canva since its so simple with only two connections. The  esp32 will be connected to my coputer along with the cmaera. I started making the code with ( lots of help) from AI. I tried to learn and udnerstand what's going on and editing some of it myself. The code launches the camera,( which will later be the camera next to the printer when I build this), every time I press M it takes a picture and saves it, so the Idea is that when the printer hits the limit switch, the computer takes a picture from the camera, which will then save the picture. Herre is a quick demo video. I then started working on the readme.MD. I added the "Why" I made this project, wiring, but still need to add BOM and code.

<img width="841" height="763" alt="image" src="https://github.com/user-attachments/assets/0e38e2a6-560e-4298-b46b-2efa25040ee2" />
<img width="749" height="1029" alt="image" src="https://github.com/user-attachments/assets/2f570b58-81e6-4768-a216-fc8f37945591" />
<img width="987" height="550" alt="Screenshot 2026-03-20 205303" src="https://github.com/user-attachments/assets/b173b7b3-ff1e-4721-abf6-de5c0a3c07ff" />
<img width="776" height="991" alt="Screenshot 2026-03-20 205254" src="https://github.com/user-attachments/assets/b81587cc-4fe0-42ed-b2f9-3e6184f6430b" />

[Watch the video](https://streamable.com/khbx4j)

 
**Total time spent: 0.6h**









