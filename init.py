from main import db,Artist,Group
db.create_all()

# artist = Artist(birth_name="Kim Ji Soo",stage_name="Jisoo",birthday="789096283")
# db.session.add(artist)
# artist = Artist(birth_name="Jennie Kim",stage_name="Jennie",birthday="821755483")
# db.session.add(artist)
# artist = Artist(birth_name="Park Chae Young",stage_name="Rose",birthday="855624283")
# db.session.add(artist)
# artist = Artist(birth_name="Lalisa Manoban/ Pranpriya Manoban",stage_name="Lisa",birthday="859425883")
# db.session.add(artist)

# db.session.commit()



# position = Position(position_name="Visual",artist_id=1)
# db.session.add(position)
# position = Position(position_name="Main Rapper",artist_id=2)
# db.session.add(position)
# position = Position(position_name="Main Vocal",artist_id=3)
# db.session.add(position)
# position = Position(position_name="Main Dancer",artist_id=4)
# db.session.add(position)

# db.session.commit()

group = Group(groupName="NCT 127",groupType="Boy Group",debutDate="July 27, 2016",company="SM Entertainment",fandomName="NCTzen",
	fandomColor="-",status="active",imgURL="https://is4-ssl.mzstatic.com/image/thumb/Music118/v4/63/cc/b4/63ccb404-eb7a-a3f0-4dc9-152540bc161f/NCT_127_Cover.jpg/268x0w.jpg",
	description="NCT 127 (엔씨티 127) is the 2nd sub-unit of the boy group NCT. The sub-unit currently consists of 10 'members': Taeil, Johnny, Taeyong, Doyoung, Yuta, Jaehyun, Win Win, Jungwoo, Mark, Haechan. NCT 127 debuted on July 7th, 2016 under SM Entertainment.")
db.session.add(group)
group = Group(groupName="Stray Kids",groupType="Boy Group",debutDate="September 13, 2018",company="JYP Entertainment",fandomName="Stay",
	fandomColor="-",status="active",imgURL="https://lastfm-img2.akamaized.net/i/u/770x0/dd9393d96f6b5b33cdd6e90f35b680fd.jpg",
	description="Stray Kids (스트레이 키즈) is a 9-member South Korean boy group under JYP Entertainment. The group consists of Bang Chan, Woojin, Lee Know, Changbin, Hyunjin, Han, Felix, Seungmin, and I.N. Stray Kids was created through the survival program with the same name, Stray Kids. Stray Kids debuted on March 25, 2018.")
db.session.add(group)
group = Group(groupName="LOONA",groupType="Girl Group",debutDate="August 20, 2018",company="Blockberry Creative",fandomName="Orbit",
	fandomColor="Holo",status="active",imgURL="https://lastfm-img2.akamaized.net/i/u/ar0/7e9fbb03749066e1d58b6e9261fdbbbc.jpg",
	description="LOONA (LOOΠΔ – 이달의 소녀) contains of 12 'members': Haseul, Vivi, Yves, JinSoul, Kim Lip, Chuu, Heejin, Hyunjin, Go Won, Choerry, Olivia Hye and Yeojin. The band is under Blockberry Creative. They debuted on August 20, 2018 with their title track “Hi High”.")
db.session.add(group)
group = Group(groupName="Seventeen",groupType="Boy Group",debutDate="",company="Pledis",fandomName="Carat",
	fandomColor="Rose Quartz and Serenity",status="active",imgURL="https://i.scdn.co/image/7b90f0bfdce832e113edba285d7aad9c283eb3d7",
	description="Saks lang")
db.session.add(group)
group = Group(groupName="SNSD",groupType="Girl Group",debutDate="",company="",fandomName="SONE",
	fandomColor="",status="",imgURL="https://lastfm-img2.akamaized.net/i/u/ar0/6cb5367bf92f061d3bfac9277161e3c2.jpg",
	description="I love you Taeyeon")
db.session.add(group)
group = Group(groupName="The Boyz",groupType="Boy Group",debutDate="",company="",fandomName="",
	fandomColor="",status="",imgURL="https://pbs.twimg.com/profile_images/942318800480772096/z8zfdksu_400x400.jpg",
	description="Pweds na")
db.session.add(group)
db.session.commit()

artist = Artist(stageName="Hyunjin",birthName="Hwang Hyunjin",nationality="Korean",gender="Male",birthday="",groupId=2,
	imgURL="https://66.media.tumblr.com/37b02b0fea4e8a3168e8e00d2c9f7631/tumblr_inline_ozl6248sJX1uprypi_540.gif")
db.session.add(artist)
artist = Artist(stageName="Woojin",birthName="Im Jaebum",nationality="Korean",gender="Male",birthday="",groupId=2,
	imgURL="https://media1.tenor.com/images/ace5f2fdd8d31c89e0c277185c5ef4a7/tenor.gif?itemid=12066202")
db.session.add(artist)
artist = Artist(stageName="Chan",birthName="Im Jaebum",nationality="Korean",gender="Male",birthday="",groupId=2,
	imgURL="https://pa1.narvii.com/6644/cbd22089050ae0a3c7c25daac0a8ccf750b37ba2_hq.gif")
db.session.add(artist)
artist = Artist(stageName="Felix",birthName="Im Jaebum",nationality="Korean",gender="Male",birthday="",groupId=2,
	imgURL="https://66.media.tumblr.com/e1c932ec2735439ace7261395f7c61c7/tumblr_pfcxbmi6yL1xo1fixo1_500.gif")
db.session.add(artist)
artist = Artist(stageName="Han",birthName="Im Jaebum",nationality="Korean",gender="Male",birthday="",groupId=2,
	imgURL="https://pa1.narvii.com/6644/cbd22089050ae0a3c7c25daac0a8ccf750b37ba2_hq.gif")
db.session.add(artist)
artist = Artist(stageName="I.N.",birthName="Im Jaebum",nationality="Korean",gender="Male",birthday="",groupId=2,
	imgURL="https://pa1.narvii.com/6694/de1e3094a68caf86d197e0663ae29db9be108102_hq.gif")
db.session.add(artist)
artist = Artist(stageName="Mingyu",birthName="Kim Mingyu",nationality="Korean",gender="Male",birthday="",groupId=4,
	imgURL="https://i.pinimg.com/originals/57/18/65/57186539846981fcc7645600595e99bc.gif")
db.session.add(artist)
artist = Artist(stageName="Kim Lip",birthName="Kim Jungeun",nationality="Korean",gender="Female",birthday="",groupId=3,
	imgURL="https://66.media.tumblr.com/5efc552c2a9106b9374c65cf81007868/tumblr_oyvfudQ2cl1qh3sm2o1_500.gif")
db.session.add(artist)


db.session.commit()

# member = Member(artist_id=1,group_name="BLACKPINK")
# db.session.add(member)
# member = Member(artist_id=2,group_name="BLACKPINK")
# db.session.add(member)
# member = Member(artist_id=3,group_name="BLACKPINK")
# db.session.add(member)
# member = Member(artist_id=4,group_name="BLACKPINK")
# db.session.add(member)

# db.session.commit()

# album = Album(album_title="Square Up",release_date="1529020800",sales=90000000,spotify_url="spotify:album:1HwIUaaEuRsxsIyssqtGLH",group_name="BLACKPINK")
# db.session.add(album)

# db.session.commit()

# song = Song(song_title="Ddu-Du Ddu-Du",album_id=1)
# db.session.add(song)
# song = Song(song_title="Forever Young",album_id=1)
# db.session.add(song)
# song = Song(song_title="Really",album_id=1)
# db.session.add(song)
# song = Song(song_title="See U Later",album_id=1)
# db.session.add(song)

# db.session.commit()