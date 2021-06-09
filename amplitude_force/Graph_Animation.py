import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


def plot_ode(t, result, N_U, u1, u2):
    plt.figure('displacement')
    plt.plot(t, result[:, 0], 'b', label='etta(t)')
    plt.plot(t, result[:, 2], 'g', label='f1(t)')
    plt.plot(t, result[:, 4], 'r', label='f2(t)')
    plt.grid()
    plt.title('etta_0 = ' + str(N_U[0]) + '; ' + 'f1_0 = ' + str(N_U[1]) + '; ' + 'f2_0 = ' + str(N_U[2]))
    plt.legend(loc='best')
    plt.xlabel('t')

    plt.figure('force')
    plt.plot(t, result[:, 0], 'b', label='T')
    plt.grid()
    plt.title('Force')
    plt.legend(loc='best')
    plt.xlabel('t')


def animations(t, result, N_U, l=0, r=1000, step=10):
    fig = plt.figure()
    ax = plt.axes(xlim=(t[l], t[r]), ylim=(-0.2, 0.2))
    ax.grid()
    plt.title('etta_0 = ' + str(N_U[0]) + '; ' + 'f1_0 = ' + str(N_U[1]) + '; ' + 'f2_0 = ' + str(N_U[2]))
    lines = [plt.plot([], [], 'b', label='etta(t)')[0], plt.plot([], [], 'g', label='f1(t)')[0], plt.plot([], [], 'r', label='f2(t)')[0]]
    legend = plt.legend(loc='best')
    patches = lines

    def init():
        lines[0].set_data([], [])
        lines[1].set_data([], [])
        lines[2].set_data([], [])
        return patches

    def animate(i):
        for j, line in enumerate(lines):
            line.set_data(t[step*i:r + step*i] - t[step*i], result[step*i:r + step*i, 2*j])
        return patches

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=1000, interval=10, blit=True)

    # anim.save('animation.gif', writer='PillowWriter', fps=20)


