# inspired from https://github.com/Cog-Creators/Red-DiscordBot/blob/develop/cogs/audio.py
import discord

TOKEN = 'LETOKENLAAAAAAAAAAA'

client = discord.Client()
voice = discord.Voice()
	
@client.event
async def on_group_join(channel,user):
	user.
	

class Playlist:
    def __init__(self, server=None, sid=None, name=None, author=None, url=None,
                 playlist=None, path=None, main_class=None, **kwargs):
        self.server = server
        self._sid = sid
        self.name = name
        # this is an id......
        self.author = author
        self.url = url
        self.main_class = main_class  # reference to Audio
        self.path = path
	
@property
    def filename(self):
        f = "data/audio/playlists"
        f = os.path.join(f, self.sid, self.name + ".txt")
        return f
		
	def _make_local_song(self, filename):
        # filename should be playlist_folder/file_name
        folder, song = os.path.split(filename)
        return Song(name=song, id=filename, title=song, url=filename,
                    webpage_url=filename)
		
	def append_song(self, author, url):
        if not self.can_edit(author):
            raise UnauthorizedSave
        elif not self.main_class._valid_playable_url(url):
            raise InvalidURL
        else:
            self.playlist.append(url)
            self.save()

    def save(self):
        dataIO.save_json(self.path, self.to_json())
		
		
 @audioset.command(name="emptydisconnect", pass_context=True)
    @checks.mod_or_permissions(manage_messages=True)
    async def audioset_emptydisconnect(self, ctx):
        """Toggles auto disconnection when everyone leaves the channel"""
        server = ctx.message.server
        settings = self.get_server_settings(server.id)
        noppl_disconnect = settings.get("NOPPL_DISCONNECT", True)
        self.set_server_setting(server, "NOPPL_DISCONNECT",
                                not noppl_disconnect)
        if not noppl_disconnect:
            await self.bot.say("If there is no one left in the voice channel"
                               " the bot will automatically disconnect after"
                               " five minutes.")
        else:
            await self.bot.say("The bot will no longer auto disconnect"
                               " if the voice channel is empty.")
        self.save_settings()
		
@playlist.command(pass_context=True, no_pm=True, name="start")
    async def playlist_start(self, ctx, name):
        """Plays a playlist."""
        server = ctx.message.server
        author = ctx.message.author
        voice_channel = ctx.message.author.voice_channel
        channel = ctx.message.channel

        caller = inspect.currentframe().f_back.f_code.co_name

        if voice_channel is None:
            await self.bot.say("You must be in a voice channel to start a"
                               " playlist.")
            return

        if self._playlist_exists(server, name):
            if not self.voice_connected(server):
                try:
                    self.has_connect_perm(author, server)
                except AuthorNotConnected:
                    await self.bot.say("You must join a voice channel before"
                                       " I can play anything.")
                    return
                except UnauthorizedConnect:
                    await self.bot.say("I don't have permissions to join your"
                                       " voice channel.")
                    return
                except UnauthorizedSpeak:
                    await self.bot.say("I don't have permissions to speak in"
                                       " your voice channel.")
                    return
                except ChannelUserLimit:
                    await self.bot.say("Your voice channel is full.")
                    return
                else:
                    await self._join_voice_channel(voice_channel)
            self._clear_queue(server)
            playlist = self._load_playlist(server, name,
                                           local=self._playlist_exists_local(
                                               server, name))
            if caller == "playlist_start_mix":
                shuffle(playlist.playlist)

            self._play_playlist(server, playlist, channel)
            await self.bot.say("Playlist queued.")
        else:
            await self.bot.say("That playlist does not exist.")


client.run(TOKEN)