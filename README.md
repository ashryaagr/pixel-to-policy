## Pixel to policy: DQN Encoders for within & cross-game reinforcement learning


### Introduction to the work

Reinforcement Learning can be applied to various tasks, and  environments. Many of these environments have a similar shared structure, which can be exploited to improve RL performance on other tasks. Transfer learning can be used to take advantage of this shared structure, by learning policies that are transferable across different tasks and environments and can lead to more efficient learning as well as improved performance on a wide range of tasks. This work explores as well as compares the performance between RL models being trained from the scratch and on different approaches of transfer learning.  Additionally, the study explores the performance of a model trained on multiple game environments, with the goal of developing a universal game-playing agent as well as transfer learning a pre-trained encoder using DQN, and continuing its training on the same game, Breakout, using the actor-critic technique that will be discussed in further detail below. Our model achieves a mean episode reward of 46.16 which even beats the human-level performance with merely 20k episodes which is significantly lower than deepmind's 1M. Even on Assault and Space invader environments, we get mean rewards of 533.42 and 402.17, which would be regarded as good performance for these environments.


### Code Structure

The code has been divided into various ipython notebook depending on the categories of experiments performed in the report. Following is a brief description of each notebook or python file.

- Atari-Breakout.ipynb : This experiment is to train DQN from scratch on breakout. You can change the environment in the code itself.
- Atari-Multiprocessing: This experiment helps in utlising multiple CPU to run multiple environments parallely to get a high sample collection rate.
- Actor Critic.ipynb: This is the code for actor critic reinforcement learning approach which leverages pretrained encoder of DQN.ß
- video.py: This is to convert video to frame rolls which have been added to report.

## Dependencies

```bash
pip install gym[atari,accept-rom-license] atari-py
pip install moviepy
```

## Pre-trained model setup

Follow the steps mentioned [here](https://github.com/floringogianu/atari-agents#how-to-use-it) to download and use pretrained models and load in the same working directory.
