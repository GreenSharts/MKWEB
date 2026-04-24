with open('mariokartweb.html', 'r') as f: content = f.read()

target = """audioManager.play('countdown');
                    setTimeout(() => {
                        rText.innerText = "3... 2... 1... GO!";
                        audioManager.play('go');
                        setTimeout(() => {
                            document.getElementById('menu-system').style.display = 'none';
                            document.getElementById('race-overlay').style.display = 'none';
                            document.getElementById('game-ui').style.display = 'block';
                            initEngine(state.character, state.vehicle, state.mode === 'gp' ? state.cup.tracks[0].index : state.track.index);
                        }, 1000);
                    }, 1000);
                }"""

replacement = """audioManager.play('countdown');
                    setTimeout(() => {
                        audioManager.play('countdown');
                        setTimeout(() => {
                            audioManager.play('countdown');
                            setTimeout(() => {
                                rText.innerText = "3... 2... 1... GO!";
                                audioManager.play('go');
                                setTimeout(() => {
                                    document.getElementById('menu-system').style.display = 'none';
                                    document.getElementById('race-overlay').style.display = 'none';
                                    document.getElementById('game-ui').style.display = 'block';
                                    initEngine(state.character, state.vehicle, state.mode === 'gp' ? state.cup.tracks[0].index : state.track.index);
                                }, 1000);
                            }, 1000);
                        }, 1000);
                    }, 1000);
                }"""

content = content.replace(target, replacement)
with open('mariokartweb.html', 'w') as f: f.write(content)
