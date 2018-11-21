from main import db,Artist,Position,Group,Album,Song,Member
db.create_all()

artist = Artist(birth_name="Kim Ji Soo",stage_name="Jisoo",birthday="789096283")
db.session.add(artist)
artist = Artist(birth_name="Jennie Kim",stage_name="Jennie",birthday="821755483")
db.session.add(artist)
artist = Artist(birth_name="Park Chae Young",stage_name="Rose",birthday="855624283")
db.session.add(artist)
artist = Artist(birth_name="Lalisa Manoban/ Pranpriya Manoban",stage_name="Lisa",birthday="859425883")
db.session.add(artist)

db.session.commit()



position = Position(position_name="Visual",artist_id=1)
db.session.add(position)
position = Position(position_name="Main Rapper",artist_id=2)
db.session.add(position)
position = Position(position_name="Main Vocal",artist_id=3)
db.session.add(position)
position = Position(position_name="Main Dancer",artist_id=4)
db.session.add(position)

db.session.commit()

group = Group(group_name="BLACKPINK",debut_date="1470619483",fandom_name="BLINK")
db.session.add(group)

db.session.commit()

member = Member(artist_id=1,group_name="BLACKPINK")
db.session.add(member)
member = Member(artist_id=2,group_name="BLACKPINK")
db.session.add(member)
member = Member(artist_id=3,group_name="BLACKPINK")
db.session.add(member)
member = Member(artist_id=4,group_name="BLACKPINK")
db.session.add(member)

db.session.commit()

album = Album(album_title="Square Up",release_date="1529020800",sales=90000000,spotify_url="spotify:album:1HwIUaaEuRsxsIyssqtGLH",group_name="BLACKPINK")
db.session.add(album)

db.session.commit()

song = Song(song_title="Ddu-Du Ddu-Du",album_id=1)
db.session.add(song)
song = Song(song_title="Forever Young",album_id=1)
db.session.add(song)
song = Song(song_title="Really",album_id=1)
db.session.add(song)
song = Song(song_title="See U Later",album_id=1)
db.session.add(song)

db.session.commit()