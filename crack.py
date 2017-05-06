import vlc
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 700))
font = pygame.font.Font(None, 50)

vol='100'
vol1='100'
vol2='100'

ratep='n'
ratet='n'



pc=True
tc=True
rc=True
pm=255
tm=255
rm=255


c1str='1'
c2str='0'

c1tstr='1'
c2tstr='0'

c1rstr='1'
c2rstr='0'


q = vlc.MediaPlayer("all.mp3")
#s = vlc.MediaPlayer("/home/andrew/Music/goa.mp3")
#first row
p = vlc.MediaPlayer("all.mp3")
#middle row
t = vlc.MediaPlayer("good.mp3")
#lastrow
r = vlc.MediaPlayer("move.mp3")

cmd=0
clock = pygame.time.Clock()


ratep=str(p.get_rate())
currentratep=p.get_rate()

ratet=str(t.get_rate())
currentratet=t.get_rate()

rater=str(r.get_rate())
currentrater=r.get_rate()

done=False
ppause=True
tpause=True
rpause=True

currentout=100000

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        p.pause()
                        ppause=not ppause


                if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    pc=not pc
                    #pm=100
                    p.audio_toggle_mute()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        t.pause()
                        tpause=not tpause

                if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                    tc=not tc
                    #tm=100
                    t.audio_toggle_mute()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_x:

                    r.pause()
                    rpause = not rpause
                if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    rc=not rc
                    #rm=100
                    r.audio_toggle_mute()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                	current1=t.get_time()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                    t.set_time(current1)

                #for p media

                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    current=p.get_time()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
                    p.set_time(current)

                #for r media

                if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                    current2=r.get_time()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    r.set_time(current2)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                    currentratep=currentratep-0.1
                    p.set_rate(currentratep)
                    ratep=str(currentratep)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    currentratep=currentratep+0.1
                    p.set_rate(currentratep)
                    ratep=str(currentratep)

                    #for t media speed

                if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                    currentratet=currentratet-0.1
                    t.set_rate(currentratet)
                    ratet=str(currentratet)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SEMICOLON:
                    currentratet=currentratet+0.1
                    t.set_rate(currentratet)
                    ratet=str(currentratet)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_PERIOD:
                    currentrater=currentrater-0.1
                    r.set_rate(currentrater)
                    rater=str(currentrater)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SLASH:
                    currentrater=currentrater+0.1
                    r.set_rate(currentrater)
                    rater=str(currentrater)


                    #input for first row
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFTBRACKET:
                	ipr1w = raw_input("What is first name? :")
                	p = vlc.MediaPlayer(str(ipr1w))
                	#input for second row
                if event.type == pygame.KEYDOWN and event.key == pygame.K_QUOTE:
                	ipr1w = raw_input("What is second name? :")
                	t = vlc.MediaPlayer(str(ipr1w))
                	#input for third row
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RSHIFT:
                	ipr1w = raw_input("What is third name? :")
                	r = vlc.MediaPlayer(str(ipr1w))










        var = p.get_time()/100

        if currentout == var:
            p.set_time(current)

        pressed = pygame.key.get_pressed()


        if pressed[pygame.K_q]:
            p.stop()
            p.play()



        if pressed[pygame.K_u]:
            currentv=p.audio_get_volume()
            vol=str(currentv)
            currentv=currentv-1
            p.audio_set_volume(currentv)

        if pressed[pygame.K_i]:
            currentv1=p.audio_get_volume()
            vol=str(currentv1)
            currentv1=currentv1+1
            p.audio_set_volume(currentv1)


        #DEFINING RATE












        if pressed[pygame.K_j]:
            currentv2=t.audio_get_volume()
            vol1=str(currentv2)
            currentv2=currentv2-1
            t.audio_set_volume(currentv2)

        if pressed[pygame.K_k]:
            currentv3=t.audio_get_volume()
            vol1=str(currentv3)
            currentv3=currentv3+1
            t.audio_set_volume(currentv3)




        if pressed[pygame.K_m]:
            currentv4=r.audio_get_volume()
            vol2=str(currentv4)
            currentv4=currentv4-1
            r.audio_set_volume(currentv4)

        if pressed[pygame.K_COMMA]:
            currentv5=r.audio_get_volume()
            vol2=str(currentv5)
            currentv5=currentv5+1
            r.audio_set_volume(currentv5)







        if pressed[pygame.K_e]:
            current = 1000000
            currentout = 1000000
            p.stop()

        if pressed[pygame.K_a]:
            t.stop()
            t.play()


        #if pressed[pygame.K_f]:
        #	current1=t.get_time()

        #	current1=current1-100
        #	t.set_time(current1)



        if pressed[pygame.K_d]:
        	t.stop()

        if pressed[pygame.K_z]:
            r.stop()
            r.play()




        if pressed[pygame.K_c]:
        	r.stop()

        if pc:
            pm=255

        else:
            pm=100

        if tc:
            tm=255

        else:
            tm=100

        if rc:
            rm=255

        else:
            rm=100





        #looping p media
        c1=p.get_length()/100
        c1con=0
        if c1>1:
            c1con=(p.get_length()/100)-20


        c1str=str(c1)
        c2=p.get_time()/100
        c2str=str(c2)
        #if c1==c2:


        run=p.is_playing()

        if run==0 and c2>c1con and ppause==True:

                p.stop()
                p.play()
                #p.set_time(250)

        #looping t media
        c1t=t.get_length()/100
        c1tcon=0
        if c1t>1:
            c1tcon=(t.get_length()/100)-20

        c1tstr=str(c1t)
        c2t=t.get_time()/100
        c2tstr=str(c2t)
        #if c1==c2:


        runt=t.is_playing()

        if runt==0 and c2t>c1tcon and tpause==True:

                t.stop()
                t.play()


        #looping r media
        c1r=r.get_length()/100
        c1rcon=0
        if c1r>1:
            c1rcon=(r.get_length()/100)-20


        c1rstr=str(c1r)
        c2r=r.get_time()/100
        c2rstr=str(c2r)
        #if c1==c2:


        runr=r.is_playing()

        if runr==0 and c2r>c1rcon and rpause==True:

                r.stop()
                r.play()







        screen.fill((0, 0, 0))
        block = font.render(vol, True, (255, pm, 255))
        rect = block.get_rect()

        rect.center = (90,30)
        screen.blit(block, rect)

        #below block:
        blockb = font.render(c1str, True, (255, pm, 255))
        rectb = blockb.get_rect()

        rectb.center = (90,90)
        screen.blit(blockb, rectb)

        #below below block:
        blockbb = font.render(c2str, True, (255, pm, 255))
        rectbb = blockbb.get_rect()

        rectbb.center = (90,150)
        screen.blit(blockbb, rectbb)

        #rate of block:
        blockbbb = font.render(ratep, True, (255, pm, 255))
        rectbbb = blockbbb.get_rect()

        rectbbb.center = (90,210)
        screen.blit(blockbbb, rectbbb)


        block1 = font.render(vol1, True, (255, tm, 255))
        rect1 = block1.get_rect()

        rect1.center = (180,30)
        screen.blit(block1, rect1)

        #below block1:
        block1b = font.render(c1tstr, True, (255, tm, 255))
        rect1b = block1b.get_rect()

        rect1b.center = (180,90)
        screen.blit(block1b, rect1b)

        #below below block1:
        block1bb = font.render(c2tstr, True, (255, tm, 255))
        rect1bb = block1bb.get_rect()

        rect1bb.center = (180,150)
        screen.blit(block1bb, rect1bb)


        #below block1 for rate of t
        block1bbb = font.render(ratet, True, (255, tm, 255))
        rect1bbb = block1bbb.get_rect()

        rect1bbb.center = (180,210)
        screen.blit(block1bbb, rect1bbb)


        block2 = font.render(vol2, True, (255, rm, 255))
        rect2 = block2.get_rect()

        rect2.center = (270,30)
        screen.blit(block2, rect2)

        #below block2:
        block2b = font.render(c1rstr, True, (255, rm, 255))
        rect2b = block2b.get_rect()

        rect2b.center = (270,90)
        screen.blit(block2b, rect2b)

        #below below block2:
        block2bb = font.render(c2rstr, True, (255, rm, 255))
        rect2bb = block2bb.get_rect()

        rect2bb.center = (270,150)
        screen.blit(block2bb, rect2bb)

        #below block2 for rate of r
        block2bbb = font.render(rater, True, (255, rm, 255))
        rect2bbb = block2bbb.get_rect()

        rect2bbb.center = (270,210)
        screen.blit(block2bbb, rect2bbb)






        pygame.display.flip()
        clock.tick(50)




print "out of while."
