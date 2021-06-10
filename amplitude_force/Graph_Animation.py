import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


def plot_ode(t, result, N_U, coeffs):

    kappa0, k0 = coeffs
    plt.figure('displacement')
    plt.plot(t, result[:, 0], 'b', label='etta(t)')
    plt.plot(t, result[:, 2], 'g', label='u1*f1(t)')
    plt.plot(t, result[:, 4], 'r', label='u2*f2(t)')
    plt.grid()
    plt.title('etta_0 = ' + str(N_U[0]) + '; ' + 'f1_0 = ' + str(N_U[1]) + '; ' + 'f2_0 = ' + str(N_U[2]))
    plt.legend(loc='best')
    plt.xlabel('t')

    force_values = [0 if etta - f1 - f2 + k0 < 0 else kappa0 * (etta - f1 - f2 + k0) for
                    etta, f1, f2 in zip(list(result[:, 0]), list(result[:, 2]), list(result[:, 4]))]

    plt.figure('force')
    plt.plot(t, force_values, 'b', label='T')
    plt.grid()
    plt.title('Force')
    plt.legend(loc='best')
    plt.xlabel('t')
    print("построил график")


def animations(t, result, N_U, coeffs, l=0, r=3000, step=30):
    kappa0, k0 = coeffs
    fig, axs = plt.subplots(2)

    for i in range(2):
        axs[i].set_xlim((t[l], t[r]))
        axs[i].grid()
    axs[0].set_ylim((N_U[0], -N_U[0]))
    axs[1].set_ylim((-0.005, 0.01))
    force_values = [0 if etta - f1 - f2 + k0 < 0 else kappa0 * (etta - f1 - f2 + k0) for
                    etta, f1, f2 in zip(list(result[:, 0]), list(result[:, 2]), list(result[:, 4]))]

    fig.suptitle('etta_0 = ' + str(N_U[0]) + '; ' + 'f1_0 = ' + str(N_U[1]) + '; ' + 'f2_0 = ' + str(N_U[2]))
    displacment = [axs[0].plot([], [], 'b', label='etta(t)')[0], axs[0].plot([], [], 'g', label='u1*f1(t)')[0], axs[0].plot([], [], 'r', label='u2*f2(t)')[0]]
    force = axs[1].plot([], [], 'b', label='force')[0]
    legend = axs[0].legend(loc='upper left')
    patches = displacment + [force]

    def init():
        displacment[0].set_data([], [])
        displacment[1].set_data([], [])
        displacment[2].set_data([], [])
        force.set_data([], [])
        return patches

    def animate(i):
        for j, line in enumerate(displacment):
            line.set_data(t[step*i:r + step*i] - t[step*i], result[step*i:r + step*i, 2*j])
        force.set_data(t[step*i:r + step*i] - t[step*i], force_values[step*i:r + step*i])
        return patches

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=300, interval=10, blit=True)
    anim.save('animation.gif', writer='PillowWriter', fps=30)

    plt.show()
    print("построил анимацию")
    return anim



