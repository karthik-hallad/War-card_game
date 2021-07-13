#card class
#suit,rank,value infomration should be therefore
#rank means the vale in 13 card deck

#creating a dictionary of values for better comparision
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
            'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')        
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
   def __init__(self):
       self.all_cards = []

       for suit in suits:
           for rank in ranks:
               #creating a card object 
               created_card=Card(suit,rank)
               self.all_cards.append(created_card)       
   def shuffle(self):
       random.shuffle(self.all_cards)
   def deal_one(self):
       return self.all_cards.pop() 

#u can aceess the card as card has a method called str
# new_deck =Deck()  // creates a new deck
# new_deck.shuffle()
# for card_object in new_deck.all_cards:  //prints all the cards in the deck
#    print(card_object)
# print(new_deck.deal_one()) //it pops out one cards and prints it
# print(len(new_deck.all_cards))//len is 51 as 1 card has been removed

# -------/ PLAYER CLASS /------
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_Cards(self,new_cards):
        if type(new_cards)==type([]):
            # appending new cards will result in nested lists
            self.all_cards.extend(new_cards)
        else:
            #for a single card object
            self.all_cards.append(new_cards)    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'

#testing
# new_player = Player('Karthik')
# print(new_player)
# mycard=Card('Hearts','Two')
# new_player.add_Cards(mycard)
# print(new_player)
# new_player.add_Cards([mycard,mycard,mycard,mycard,mycard])
# print(new_player)
# #out
# Player Karthik has 0 cards
# Player Karthik has 1 cards
# Player Karthik has 6 cards

########GAME LOGIC #########
#Game setup
player_one=Player('One')
player_two=Player('Two')

# creating a list and shuffling it
new_deck=Deck()
new_deck.shuffle()

# disributing the cards 26 to each
for x in range(26):
    player_one.add_Cards(new_deck.deal_one())
    player_two.add_Cards(new_deck.deal_one())

game_on=True

#while game_on
round_num=0
while game_on:
    round_num+=1
    if(round_num==25001):
        print("Round Limit Exceeded")
        print("The Game is a Tie")
        break
    print(f"Currently on round {round_num}")

    #we need both break and gameon as False as without it the whole while loop gets executed
    if(len(player_one.all_cards)==0):
        print("Player One, out of Cards! Player Two wins")
        game_on=False
        break

    if(len(player_two.all_cards)==0):
        print("Player Two, out of Cards! Player One wins")
        game_on=False
        break    
    
    #Starting a new round
    #below lists refer to the cards on the table
    player_one_cards=[]
    player_one_cards.append(player_one.remove_one())

    player_two_cards=[]
    player_two_cards.append(player_two.remove_one())

    #while at_war
    at_war=True
    while at_war:
        if player_one_cards[-1].value>player_two_cards[-1].value:
# player_one gets both the cards which are in table ir one from each player            
            player_one.add_Cards(player_one_cards)
            player_one.add_Cards(player_two_cards)
            at_war=False

        elif player_one_cards[-1].value<player_two_cards[-1].value:
            player_two.add_Cards(player_one_cards)
            player_two.add_Cards(player_two_cards)
            at_war=False 

        else:
            print("YOU ARE AT WAR")
            at_war=True     
            #checking if both players are eligible for war or not
            #assuming that the palyers will give 3 cards when in war
            if len(player_one.all_cards) <3:
                print(" Player one cannot declare war")
                print("Player Two wins!!")
                game_on=False
                break
            elif len(player_two.all_cards) <3:
                print(" Player two cannot declare war")
                print("Player ONE wins!!")
                game_on=False
                break
            #using range and removing 2 cards from each player
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

                #-------------SAMPLE OUTPUT--------#
# Currently on round 1
# Currently on round 2
# YOU ARE AT WAR      
# Currently on round 3
# Currently on round 4
# Currently on round 5
# Currently on round 6
# Currently on round 7
# Currently on round 8
# Currently on round 9
# Currently on round 10
# Currently on round 11
# Currently on round 12
# Currently on round 13
# Currently on round 14
# Currently on round 15
# Currently on round 16
# Currently on round 17
# Currently on round 18
# Currently on round 19
# Currently on round 20
# Currently on round 21
# Currently on round 22
# Currently on round 23
# Currently on round 24
# Currently on round 25
# Currently on round 26
# Currently on round 27
# Currently on round 28
# Currently on round 29
# Currently on round 30
# Currently on round 31
# YOU ARE AT WAR
# Currently on round 32
# Currently on round 33
# Currently on round 34
# Currently on round 35
# Currently on round 36
# Currently on round 37
# Currently on round 38
# Currently on round 39
# Currently on round 40
# Currently on round 41
# Currently on round 42
# YOU ARE AT WAR
# Currently on round 43
# Currently on round 44
# Currently on round 45
# Currently on round 46
# Currently on round 47
# Currently on round 48
# Currently on round 49
# Currently on round 50
# Currently on round 51
# Currently on round 52
# YOU ARE AT WAR
# Currently on round 53
# Currently on round 54
# Currently on round 55
# Currently on round 56
# Currently on round 57
# Currently on round 58
# Currently on round 59
# Currently on round 60
# Currently on round 61
# Currently on round 62
# Currently on round 63
# YOU ARE AT WAR
# Currently on round 64
# Currently on round 65
# Currently on round 66
# Currently on round 67
# Currently on round 68
# Currently on round 69
# Currently on round 70
# YOU ARE AT WAR
# Currently on round 71
# Currently on round 72
# Currently on round 73
# Currently on round 74
# Currently on round 75
# Currently on round 76
# Currently on round 77
# Currently on round 78
# Currently on round 79
# Currently on round 80
# Currently on round 81
# Currently on round 82
# Currently on round 83
# Currently on round 84
# Currently on round 85
# Currently on round 86
# Currently on round 87
# Currently on round 88
# Currently on round 89
# Currently on round 90
# Currently on round 91
# Currently on round 92
# Currently on round 93
# Currently on round 94
# Currently on round 95
# Currently on round 96
# Currently on round 97
# Currently on round 98
# Currently on round 99
# Currently on round 100
# Currently on round 101
# Currently on round 102
# Currently on round 103
# Currently on round 104
# Currently on round 105
# Currently on round 106
# Currently on round 107
# Currently on round 108
# Currently on round 109
# Currently on round 110
# Currently on round 111
# Currently on round 112
# Currently on round 113
# Currently on round 114
# Currently on round 115
# Currently on round 116
# Currently on round 117
# YOU ARE AT WAR
# Currently on round 118
# Currently on round 119
# Currently on round 120
# Currently on round 121
# Currently on round 122
# Currently on round 123
# Currently on round 124
# Currently on round 125
# Currently on round 126
# Currently on round 127
# Currently on round 128
# Currently on round 129
# Currently on round 130
# Currently on round 131
# Currently on round 132
# Currently on round 133
# Currently on round 134
# Currently on round 135
# Currently on round 136
# Currently on round 137
# Currently on round 138
# Currently on round 139
# Currently on round 140
# Currently on round 141
# Currently on round 142
# Currently on round 143
# Currently on round 144
# Currently on round 145
# Currently on round 146
# Currently on round 147
# Currently on round 148
# Currently on round 149
# Currently on round 150
# Currently on round 151
# Currently on round 152
# Currently on round 153
# Currently on round 154
# Currently on round 155
# Currently on round 156
# Currently on round 157
# Currently on round 158
# Currently on round 159
# Currently on round 160
# Currently on round 161
# Currently on round 162
# Currently on round 163
# Currently on round 164
# Currently on round 165
# Currently on round 166
# Currently on round 167
# Currently on round 168
# Currently on round 169
# Currently on round 170
# Currently on round 171
# Currently on round 172
# Currently on round 173
# Currently on round 174
# Currently on round 175
# Currently on round 176
# Currently on round 177
# Currently on round 178
# Currently on round 179
# Currently on round 180
# Currently on round 181
# Currently on round 182
# Currently on round 183
# Currently on round 184
# Currently on round 185
# Currently on round 186
# Currently on round 187
# Currently on round 188
# Currently on round 189
# Currently on round 190
# Currently on round 191
# Currently on round 192
# Currently on round 193
# Currently on round 194
# Currently on round 195
# YOU ARE AT WAR
# Currently on round 196
# Currently on round 197
# Currently on round 198
# Currently on round 199
# Currently on round 200
# Currently on round 201
# Currently on round 202
# Currently on round 203
# Currently on round 204
# Currently on round 205
# Currently on round 206
# Currently on round 207
# Currently on round 208
# Currently on round 209
# Currently on round 210
# Currently on round 211
# YOU ARE AT WAR
# Currently on round 212
# Currently on round 213
# Currently on round 214
# Currently on round 215
# Currently on round 216
# Currently on round 217
# Currently on round 218
# Currently on round 219
# Currently on round 220
# Currently on round 221
# Currently on round 222
# Currently on round 223
# Currently on round 224
# Currently on round 225
# Currently on round 226
# Currently on round 227
# Currently on round 228
# Currently on round 229
# Currently on round 230
# Currently on round 231
# Currently on round 232
# Currently on round 233
# Currently on round 234
# Currently on round 235
# Currently on round 236
# Currently on round 237
# Currently on round 238
# Currently on round 239
# Currently on round 240
# Currently on round 241
# Currently on round 242
# Currently on round 243
# Currently on round 244
# Currently on round 245
# Currently on round 246
# Currently on round 247
# Currently on round 248
# Currently on round 249
# Currently on round 250
# Currently on round 251
# Currently on round 252
# Currently on round 253
# Currently on round 254
# Currently on round 255
# Currently on round 256
# Currently on round 257
# Currently on round 258
# Currently on round 259
# Currently on round 260
# Currently on round 261
# Currently on round 262
# YOU ARE AT WAR
# Currently on round 263
# Currently on round 264
# Currently on round 265
# Currently on round 266
# Currently on round 267
# Currently on round 268
# Currently on round 269
# Currently on round 270
# Currently on round 271
# Currently on round 272
# YOU ARE AT WAR
# Currently on round 273
# Currently on round 274
# Currently on round 275
# Currently on round 276
# Currently on round 277
# Currently on round 278
# Currently on round 279
# Currently on round 280
# Currently on round 281
# Currently on round 282
# Currently on round 283
# Currently on round 284
# Currently on round 285
# Currently on round 286
# Currently on round 287
# Currently on round 288
# Currently on round 289
# Currently on round 290
# Currently on round 291
# YOU ARE AT WAR
# Currently on round 292
# Currently on round 293
# Currently on round 294
# Currently on round 295
# Currently on round 296
# Currently on round 297
# Currently on round 298
# Currently on round 299
# Currently on round 300
# Currently on round 301
# Currently on round 302
# Currently on round 303
# Currently on round 304
# Currently on round 305
# Currently on round 306
# Currently on round 307
# Currently on round 308
# Currently on round 309
# Currently on round 310
# Currently on round 311
# Currently on round 312
# Currently on round 313
# Currently on round 314
# Currently on round 315
# Currently on round 316
# Currently on round 317
# Currently on round 318
# Currently on round 319
# Currently on round 320
# Currently on round 321
# Currently on round 322
# Currently on round 323
# Currently on round 324
# Currently on round 325
# Currently on round 326
# Currently on round 327
# Currently on round 328
# Currently on round 329
# Currently on round 330
# Currently on round 331
# Currently on round 332
# Currently on round 333
# Currently on round 334
# Currently on round 335
# Currently on round 336
# Currently on round 337
# Currently on round 338
# Currently on round 339
# Currently on round 340
# Currently on round 341
# Currently on round 342
# Currently on round 343
# Currently on round 344
# Currently on round 345
# Currently on round 346
# Currently on round 347
# Currently on round 348
# Currently on round 349
# Currently on round 350
# Currently on round 351
# Currently on round 352
# Currently on round 353
# Currently on round 354
# Currently on round 355
# Currently on round 356
# Currently on round 357
# Currently on round 358
# Currently on round 359
# Currently on round 360
# Currently on round 361
# Currently on round 362
# Currently on round 363
# Currently on round 364
# Currently on round 365
# Currently on round 366
# Currently on round 367
# Currently on round 368
# Currently on round 369
# Currently on round 370
# Currently on round 371
# Currently on round 372
# Currently on round 373
# Currently on round 374
# Currently on round 375
# Currently on round 376
# Currently on round 377
# Currently on round 378
# Currently on round 379
# Currently on round 380
# Currently on round 381
# Currently on round 382
# Currently on round 383
# Currently on round 384
# Currently on round 385
# Currently on round 386
# Currently on round 387
# Currently on round 388
# Currently on round 389
# Currently on round 390
# Currently on round 391
# Currently on round 392
# Currently on round 393
# Currently on round 394
# Currently on round 395
# Currently on round 396
# Currently on round 397
# Currently on round 398
# Currently on round 399
# Currently on round 400
# Currently on round 401
# Currently on round 402
# Currently on round 403
# Currently on round 404
# YOU ARE AT WAR
# Currently on round 405
# Currently on round 406
# Currently on round 407
# Currently on round 408
# Currently on round 409
# Currently on round 410
# Currently on round 411
# Currently on round 412
# Currently on round 413
# Currently on round 414
# Currently on round 415
# Currently on round 416
# Currently on round 417
# Currently on round 418
# Currently on round 419
# Currently on round 420
# Currently on round 421
# Currently on round 422
# Currently on round 423
# Currently on round 424
# Currently on round 425
# Currently on round 426
# Currently on round 427
# Currently on round 428
# Currently on round 429
# Currently on round 430
# Currently on round 431
# Currently on round 432
# Currently on round 433
# Currently on round 434
# Currently on round 435
# YOU ARE AT WAR
# Currently on round 436
# Currently on round 437
# Currently on round 438
# Currently on round 439
# Currently on round 440
# Currently on round 441
# Currently on round 442
# Currently on round 443
# Currently on round 444
# Currently on round 445
# Currently on round 446
# Currently on round 447
# Currently on round 448
# Currently on round 449
# Currently on round 450
# YOU ARE AT WAR
# Currently on round 451
# Currently on round 452
# Currently on round 453
# Currently on round 454
# Currently on round 455
# Currently on round 456
# Currently on round 457
# Currently on round 458
# Currently on round 459
# Currently on round 460
# Currently on round 461
# Currently on round 462
# Currently on round 463
# Currently on round 464
# Currently on round 465
# Currently on round 466
# Currently on round 467
# Currently on round 468
# Currently on round 469
# Currently on round 470
# Currently on round 471
# Currently on round 472
# Currently on round 473
# Currently on round 474
# Currently on round 475
# Currently on round 476
# Currently on round 477
# Currently on round 478
# Currently on round 479
# Currently on round 480
# Currently on round 481
# Currently on round 482
# Currently on round 483
# Currently on round 484
# Currently on round 485
# Currently on round 486
# Currently on round 487
# Currently on round 488
# Currently on round 489
# Currently on round 490
# Currently on round 491
# YOU ARE AT WAR
# Currently on round 492
# Currently on round 493
# Currently on round 494
# Currently on round 495
# Currently on round 496
# Currently on round 497
# Currently on round 498
# Currently on round 499
# Currently on round 500
# Currently on round 501
# Currently on round 502
# Currently on round 503
# Currently on round 504
# Currently on round 505
# Currently on round 506
# Currently on round 507
# Currently on round 508
# Currently on round 509
# Currently on round 510
# Currently on round 511
# Currently on round 512
# Currently on round 513
# Currently on round 514
# Currently on round 515
# Currently on round 516
# Currently on round 517
# Currently on round 518
# Currently on round 519
# Currently on round 520
# Currently on round 521
# Currently on round 522
# Currently on round 523
# Currently on round 524
# Currently on round 525
# Currently on round 526
# Currently on round 527
# Currently on round 528
# Currently on round 529
# Currently on round 530
# Currently on round 531
# Currently on round 532
# Currently on round 533
# Currently on round 534
# Currently on round 535
# Currently on round 536
# Currently on round 537
# Currently on round 538
# Currently on round 539
# Currently on round 540
# Currently on round 541
# Currently on round 542
# Currently on round 543
# Currently on round 544
# Currently on round 545
# Currently on round 546
# Currently on round 547
# Currently on round 548
# Currently on round 549
# Currently on round 550
# Currently on round 551
# Currently on round 552
# Currently on round 553
# Currently on round 554
# Currently on round 555
# Currently on round 556
# Currently on round 557
# Currently on round 558
# Currently on round 559
# Currently on round 560
# Currently on round 561
# Currently on round 562
# Currently on round 563
# Currently on round 564
# Currently on round 565
# Currently on round 566
# Currently on round 567
# Currently on round 568
# Currently on round 569
# Currently on round 570
# Currently on round 571
# Currently on round 572
# Currently on round 573
# Currently on round 574
# Currently on round 575
# Currently on round 576
# Currently on round 577
# Currently on round 578
# Currently on round 579
# Currently on round 580
# Currently on round 581
# Currently on round 582
# Currently on round 583
# Currently on round 584
# Currently on round 585
# Currently on round 586
# YOU ARE AT WAR
#  Player two cannot declare war
# Player ONE wins!!