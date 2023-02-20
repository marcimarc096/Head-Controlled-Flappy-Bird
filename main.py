# Flappy Bird Computer Vision Project

"""Importing the required Libraries"""
# Import the `subprocess` module for executing shell commands
import subprocess

# Import the `os` module for interacting with the operating system
import os

# Import the `sys` module for manipulating different parts of the Python runtime environment
import sys

# Import the `time` module for working with time-related functions
import time

# Import the `random` module for generating random values
import random

# Import the `pygame` module for developing games in Python
import pygame

# Import the `cv2` module (OpenCV) for computer vision tasks
import cv2 as cv

# Import the `mediapipe` module for face detection
import mediapipe

# Import the `deque` module from the `collections` package for keeping track of the pipes
from collections import deque

# Import the `button` module
import button

# Import the `playsound` function from the `playsound` module for playing audio files
from playsound import playsound

# Import the `mixer` module from the `pygame` library for working with audio and sound
from pygame import mixer

class Flappy_Game:
    def __init__(self):

        # Image files
        self.FLAG = True  # Flag for ending the game loop
        self.theme = "theme1.jpg"  # Background image file for the game screen
        self.window_game_size = None  # Size of the game screen window
        self.window_x_axis = None  # X-axis position of the game screen window
        self.window_y_axis = None  # Y-axis position of the game screen window
        self.game_screen = None  # Pygame display surface for the game screen
        self.Video_capturing = None  # Object for capturing video from a camera
        self.font = "purisa.tff"  # Font file for text rendering in the game
        self.color = (0, 0, 0)  # Color for text rendering in the game
        self.image = "black_ghost_sprite.png"  # Image file for the game character
        self.pipe_image_file = "Pipe1.png"  # Image file for the pipes in the game

        # Pipe initializations
        self.pip_image = None  # Image of the pipe
        self.pipe_frames = None  # List of frames for the pipe animation
        self.pipe_starting_template = None  # Starting template for the pipes in the game

        # Character initializations
        self.frame = None  # Frame of the game character
        self.character = None  # Image of the game character
        self.character_frame = None  # List of frames for the game character animation

        self.thickness = 1  # Thickness of lines and circles in the game
        self.circle_radius = 1  # Radius of circles in the game
        self.camera_id = 0  # Video capturing from the camera (0 is the id of the camera)
        self.space_between_pipes = 250  # Space between consecutive pipes in the game
        self.divide_factor = 6  # Factor for dividing the height of the game screen

        # Game variables
        self.Clock = None  # Clock for tracking the time in the game
        self.Game_Stage = None  # Pygame surface for the game stage
        self.Pipe_spawning = None  # Pipe spawning event in the game
        self.Pipe_time_diff = None  # Time difference between two pipe spawning events
        self.Pipe_spawn_distance = None  # Distance between two pipe spawning events
        self.update_Score = None  # Event for updating the score in the game
        self.game_running = None  # Flag for checking if the game is running
        self.game_score = None  # Current score of the game
        self.game_points = None  # Points earned in the game
        self.pipe_speed = None  # Speed of the pipes in the game
        self.timer = None  # Timer for tracking the time in the game

        self.detection_position = 94  # Position for detection in the game

    def playing_character(self, image):
        # function to set the image of the playing character
        self.image = image

    def character_(self):
        # function to load the character image and resize it to a smaller size
        self.character = pygame.image.load(self.image, "Game Character")
        width = self.character.get_width() / self.divide_factor
        height = self.character.get_height() / self.divide_factor
        self.character = pygame.transform.scale(self.character, (width, height))
        return self.character

    def speed(self):
        # function to calculate the speed of the pipes
        return self.Pipe_spawn_distance / self.Pipe_time_diff

    def game_settings(self):
        # function to initialize the game settings
        self.Clock, self.Game_Stage, self.Pipe_spawning, self.Pipe_time_diff = time.time(), 1, 0, 40
        self.Pipe_spawn_distance, self.game_score = 500, 0
        self.game_running = True
        self.update_Score = False
        self.pipe_speed = self.speed()
        self.game_points = 1
        self.timer = 1

    def game_over_part(self):
        # function to show the game over message, score and restart time
        surface = pygame.display.set_mode(self.window_game_size)
        surface.fill((0, 0, 0))
        pygame.display.flip()

        t = 5000

        self.color = (255, 0, 0)
        text = pygame.font.SysFont(self.font, 64).render("GAME OVER!", True, self.color)
        text1 = pygame.font.SysFont(self.font, 64).render("SCORE = {}".format(self.game_score), True, self.color)
        self.color = (0, 255, 236)
        text2 = pygame.font.SysFont(self.font, 64).render("RESTART IN = {}s".format(t / 1000), True, self.color)

        text_frame = text.get_rect()
        text1_frame = text1.get_rect()
        text2_frame = text1.get_rect()

        text_frame.center = (self.window_x_axis / 2, self.window_y_axis / 6)
        text1_frame.center = (self.window_x_axis / 2, self.window_y_axis / 3)
        text2_frame.center = (self.window_x_axis / 2.55, self.window_y_axis / 2)

        self.game_screen.blit(text, text_frame)
        self.game_screen.blit(text1, text1_frame)
        self.game_screen.blit(text2, text2_frame)
        pygame.display.update()
        pygame.time.wait(t)

    def stage_text(self):
        """Displays the current stage of the game"""
        text = pygame.font.SysFont(self.font, 25).render(f'Stage: {self.Game_Stage}', True, self.color)
        text_rect = text.get_rect()
        text_rect.center = (50, 25)
        self.game_screen.blit(text, text_rect)

    def score_text(self):
        """Displays the current score of the player"""
        text = pygame.font.SysFont(self.font, 25).render(f'Score: {self.game_score}', True, self.color)
        text_rect = text.get_rect()
        text_rect.center = (50, 50)
        self.game_screen.blit(text, text_rect)

    def timings(self):
        """Updates the time_difference between pipes and the stage of the game"""
        self.Pipe_time_diff *= 5 / 6
        self.Game_Stage += 1
        self.Clock = time.time()

    def Exit(self):
        """Exits the game by releasing the video capture, closing all windows and quitting pygame"""
        self.Video_capturing.release()
        cv.destroyAllWindows()  # Destroying all Windows Created.
        pygame.quit()  # Quitting pygame.
        sys.exit()  # For exiting the program.

    def again(self):
        """Returns False, information not provided in the code"""
        print("In Here")
        return False

    def Game_Working(self):
        """
        This function combines all the necessary components for the game to work:
        facial recognition, drawing the mesh on the face, initiating Pygame,
        capturing video from the camera, setting the game character, and setting up the pipes.
        It also starts the background music.
        """

        # Importing MediaPipe components for facial recognition and mesh drawing
        mp_face_recognition = mediapipe.solutions.drawing_utils
        mp_face_recognition_styles = mediapipe.solutions.drawing_styles
        mp_face_mesh = mediapipe.solutions.face_mesh

        # Setting the specifications for drawing on the face
        drawing_specifications = mp_face_recognition.DrawingSpec(thickness=self.thickness,
                                                                 circle_radius=self.circle_radius)

        # Initializing Pygame
        pygame.init()

        # Capturing video from the camera
        self.Video_capturing = cv.VideoCapture(self.camera_id)

        # Setting the game window size
        self.window_game_size = (self.Video_capturing.get(cv.CAP_PROP_FRAME_WIDTH),
                                 self.Video_capturing.get(cv.CAP_PROP_FRAME_HEIGHT))

        # Setting the x and y axis of the window
        self.window_x_axis = self.window_game_size[0]
        self.window_y_axis = self.window_game_size[1]

        # Setting the game screen in Pygame
        self.game_screen = pygame.display.set_mode(self.window_game_size)

        # Setting the game character
        self.character = pygame.image.load(self.image, "Game Character")
        width = self.character.get_width() / self.divide_factor
        height = self.character.get_height() / self.divide_factor
        self.character = pygame.transform.scale(self.character, (width, height))
        self.character_frame = self.character.get_rect()

        # Centering the character in the game window
        x = self.window_x_axis // 6
        y = self.window_y_axis // 2
        self.character_frame.center = (self.window_x_axis // 6, self.window_y_axis // 2)

        # Setting up the pipes for the game
        self.pipe_frames = deque()
        self.pip_image = pygame.image.load(self.pipe_image_file, "Pipe Image")
        self.pipe_starting_template = self.pip_image.get_rect()
        self.game_settings()

        # Initializing background music
        mixer.init()
        mixer.music.load("Background_sound.mp3")
        mixer.music.play()

        with mp_face_mesh.FaceMesh(max_num_faces=1,
                                   refine_landmarks=True,
                                   min_detection_confidence=0.5,
                                   min_tracking_confidence=0.5) as face_mesh:

            flag = True
            while flag:  # Starting an infinite loop.

                flag1 = not self.game_running
                if flag1:
                    mixer.init()
                    mixer.music.load('game_over.mp3')
                    mixer.music.play()

                    f = self.game_over_part()
                    # self.Exit()
                    self.Video_capturing.release()
                    cv.destroyAllWindows()  # Destroying all Windows Created.
                    pygame.quit()  # Quitting pygame

                    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

                for event in pygame.event.get():  # For stopping the game.
                    # Close the game if you quit by ctrl + w or Crossing.
                    if event.type == pygame.QUIT:
                        playsound("mouse_click.mp3")
                        self.Exit()

                # Capturing the frames and the return value.
                ret, self.frame = self.Video_capturing.read()
                if not ret:  # if returned value is false and no frame is captured.
                    print("No Frame Got...")
                    continue

                self.game_screen.fill((150, 150, 150))  # fill with some random color later we will overwrite this.

                """Face Mesh, making our frame writable false so it speeds up the face detection processes"""

                state = False
                self.frame.flags.writeable = state
                self.frame = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)  # Converts the BGR frame to RGB
                results = face_mesh.process(self.frame)
                self.frame.flags.writeable = not state

                """Bird Position Adjustments"""
                if results.multi_face_landmarks and len(results.multi_face_landmarks) > 0:

                    marker = results.multi_face_landmarks[0].landmark[self.detection_position].y
                    self.character_frame.centery = +self.window_y_axis/2 + (marker - 0.5) * 1.5 * self.window_y_axis

                    if self.character_frame.top < 0:
                        self.character_frame.y = 0

                    if self.character_frame.bottom > self.window_y_axis:
                        self.character_frame.y = self.window_y_axis - self.character_frame.height

                """Swapping of axis is needed.by mirroring the frame it will be more natural """

                self.frame = cv.flip(self.frame, 1).swapaxes(0, 1)

                """Update the pipes"""

                for pipe_frame in self.pipe_frames:
                    pipe_frame[0].x -= self.speed()
                    pipe_frame[1].x -= self.speed()

                # self.del_pipes_left()

                len_pipe_frames = len(self.pipe_frames)
                if len_pipe_frames > 0 and self.pipe_frames[0][0].right < 0:
                    self.pipe_frames.popleft()

                """Update screen"""
                # Putting the frames onto the screen

                imp = pygame.image.load(self.theme).convert()
                self.game_screen.blit(imp, (0, 0))
                if self.FLAG: pygame.surfarray.blit_array(self.game_screen, self.frame)
                self.game_screen.blit(self.character, self.character_frame)
                counter = True
                for pipe_frame in self.pipe_frames:
                    # Check if bird went through to update score

                    if pipe_frame[0].left <= self.character_frame.x <= pipe_frame[0].right:
                        counter = False

                        if not self.update_Score:
                            self.game_score += self.game_points
                            self.update_Score = True
                    # Update screen

                    self.game_screen.blit(self.pip_image, pipe_frame[1])
                    self.game_screen.blit(pygame.transform.flip(self.pip_image, 0, 1), pipe_frame[0])

                if counter:
                    self.update_Score = False

                """Stage and Score Text"""
                self.stage_text()
                self.score_text()

                pygame.display.flip()

                # Check if bird collides with the pipes
                if any([self.character_frame.colliderect(pipe_frame[0]) or
                        self.character_frame.colliderect(pipe_frame[1])
                        for pipe_frame in self.pipe_frames]):
                    # Stop the background music
                    mixer.music.stop()
                    # Play sound effect for collision
                    playsound("ouch.mp3")
                    # Set game running too false to end the game
                    self.game_running = False

                # Check if it's time to spawn new pipes
                if self.Pipe_spawning == 0:
                    # Create a copy of the pipe starting template
                    top = self.pipe_starting_template.copy()
                    # Randomly position the top pipe
                    top.x = random.randint(self.window_x_axis - 100, self.window_x_axis)
                    top.y = random.randint(110 - 1000, self.window_y_axis - 120 - self.space_between_pipes - 1000) \
                            + random.randint(-100, 50)

                    # Create a copy of the pipe starting template
                    bottom = self.pipe_starting_template.copy()
                    # Randomly position the bottom pipe
                    bottom.x = random.randint(self.window_x_axis - 100, self.window_x_axis)
                    bottom.y = top.y + random.randint(900, 1000) + self.space_between_pipes

                    # Appending the Pipes
                    self.pipe_frames.append([top, bottom])

                self.Pipe_spawning += self.timer
                if self.Pipe_spawning >= self.Pipe_time_diff:
                    self.Pipe_spawning = 0

                # Update stage
                if time.time() - self.Clock >= 10:
                    # self.Pipe_time_diff *= 5 / 6
                    # self.Game_Stage += 1
                    # self.Clock = time.time()

                    self.timings()
                # Displaying


if __name__ == "__main__":
    print("Game Starting....")
    # obj = Flappy_Game()
    # obj.Game_Working()
    # create display window
    SCREEN_HEIGHT = 600
    SCREEN_WIDTH = 800

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Main Menu')

    # create a surface object, image is drawn on it.
    imp = pygame.image.load("Welcome.png").convert()

    # load button images
    default_img = pygame.image.load('button_default.png').convert_alpha()
    jungle_img = pygame.image.load('button_jungle.png').convert_alpha()
    space_img = pygame.image.load('button_space.png').convert_alpha()
    ocean_img = pygame.image.load('button_ocean.png').convert_alpha()

    # exit_img = pygame.image.load('exit_btn.png').convert_alpha()

    # create button instances
    Default_button = button.Button(200, 205, default_img, 0.8)
    Jungle_button = button.Button(200, 300, jungle_img, 0.8)
    Space_button = button.Button(200, 400, space_img, 0.8)
    Ocean_button = button.Button(200, 500, ocean_img, 0.8)

    # exit_button = button.Button(450, 200, exit_img, 0.8)
    screen.blit(imp, (0, 0))

    # paint screen one time
    pygame.display.flip()
    # game loop
    run = True


    while run:

        if Default_button.draw(screen):
            playsound("mouse_click.mp3")

            pygame.quit()
            obj = Flappy_Game()
            obj.Game_Working()
            again = obj.again()


        # If Space Button Is Pressed
        if Space_button.draw(screen):
            playsound("mouse_click.mp3")

            pygame.quit()
            obj = Flappy_Game()
            obj.FLAG = False
            obj.Game_Working()
            again = obj.again()

        # If Jungle Button Is Pressed
        if Jungle_button.draw(screen):
            playsound("mouse_click.mp3")

            pygame.quit()
            obj = Flappy_Game()
            obj.FLAG = False
            obj.theme = "theme2.jpg"
            obj.image = "hat_guy.png"
            obj.pipe_image_file = "Pipe2.png"
            obj.Game_Working()
            again = obj.again()

        # If Ocean Button Is Pressed
        if Ocean_button.draw(screen):
            playsound("mouse_click.mp3")

            pygame.quit()
            obj = Flappy_Game()
            obj.FLAG = False
            obj.theme = "theme3.png"
            obj.image = "fish.png"
            obj.pipe_image_file = "Pipe3.png"
            obj.Game_Working()
            again = obj.again()

        # If The
        for event in pygame.event.get():
            # quit game

            if event.type == pygame.QUIT:
                playsound("mouse_click.mp3")
                run = False

        pygame.display.update()
    pygame.quit()
