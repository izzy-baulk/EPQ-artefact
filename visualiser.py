#structure from Davies, A (2022) kinematics_visualisaion.py (Commit 18da47a)[Source code]. https://github.com/ad-1/3DKinematicsVisualisation/blob/master/kinematics_visualisaion.py
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import animation
class Animator:
    def __init__(self, simulation_results1, simulation_results2, simulation_results3):
        # load in dataframes from modelling stage 
        self.simulation_results1 = simulation_results1
        self.simulation_results2 = simulation_results2
        self.simulation_results3 = simulation_results3
        #  configure plots and data structures
        self.fig = plt.figure(figsize=(15, 8))
        self.fig.subplots_adjust(left=0.05,
                                 bottom=None,
                                 right=0.95,
                                 top=None,
                                 wspace=None,
                                 hspace=0.28)
        gs = gridspec.GridSpec(3, 3)
        #create main animation plot
        self.ax1 = self.fig.add_subplot(gs[:, 0], projection='3d')

        #velocity and magnitude subplots for electron
        self.axElectronA = self.fig.add_subplot(gs[2, 2])
        self.axElectronB = self.axElectronA.twinx()
        self.rvte, = self.axElectronA.plot([], [], 'g-')
        self.vvte, = self.axElectronB.plot([], [], 'r-')
        self.rmag_texte = self.axElectronB.text(0, 0, '', size=12, color='b')

        #velocity and magnitude subplots incoming photon
        self.axPhoton1A = self.fig.add_subplot(gs[0, 2])
        self.axPhoton1B = self.axPhoton1A.twinx()
        self.rvtp1, = self.axPhoton1A.plot([], [], 'g-')
        self.vvtp1, = self.axPhoton1B.plot([], [], 'r-')
        self.rmag_textp1 = self.axPhoton1B.text(0, 0, '', size=12, color='b')        

        #outgoing photon
        self.axPhoton2A = self.fig.add_subplot(gs[1, 2])
        self.axPhoton2B = self.axPhoton2A.twinx()
        self.rvtp2, = self.axPhoton2A.plot([], [], 'g-')
        self.vvtp2, = self.axPhoton2B.plot([], [], 'r-')
        self.rmag_textp2 = self.axPhoton2B.text(0, 0, '', size=12, color='b')

        self.set_axes_limits()
        self.fig.tight_layout() #set appropriate spacing between plots

        #create a trajectory object for each particle
        self.trajectory1, = self.ax1.plot([], [], [], color='magenta', markersize=1)
        self.trajectory2, = self.ax1.plot([], [], [], color='purple', markersize=1)
        self.trajectory3, = self.ax1.plot([], [], [], color='blue', markersize=1)

    def draw_xyz_axis(self, x_lims, y_lims, z_lims):
        #draw origin and axes on main plot
        self.ax1.plot(0, 0, 0, 'ko', label='Origin')
        self.ax1.plot(x_lims, [0, 0], [0, 0], 'k-', lw=1) 
        self.ax1.plot([0, 0], y_lims, [0, 0], 'k-', lw=1)
        self.ax1.plot([0, 0], [0, 0], z_lims, 'k-', lw=1)
        self.text_artist_3d('x', 'k', x_lims[0], 0, 0)
        self.text_artist_3d('y', 'k', 0, y_lims[0], 0)
        self.text_artist_3d('z', 'k', 0, 0, z_lims[0])
        self.ax1.set_xlabel('x')
        self.ax1.set_ylabel('y')
        self.ax1.set_zlabel('z')  

    def text_artist_3d(self, text, color, x=0, y=0, z=0):
        #create text instance
        return self.ax1.text(x, y, z, text, size=11, color=color)

    def set_axes_limits(self):
        #set limits of main plot to (500,500,500) and draw axes accordingly
        x_lims = [-500, 500]
        y_lims = [-500, 500]
        z_lims = [-500, 500]

        self.ax1.set_xlim3d(x_lims[0], x_lims[1])
        self.ax1.set_ylim3d(y_lims[0], y_lims[1])
        self.ax1.set_zlim3d(z_lims[0], z_lims[1])
        self.draw_xyz_axis(x_lims, y_lims, z_lims)
        
        #get limits for subplots from time period of simulation data
        t_lims1 = self.get_limits1(['t'], '')
        t_lims2 = self.get_limits2(['t'], '')
        if t_lims1 > t_lims2:
            t_lims = t_lims1
        else:
            t_lims = t_lims2       

        #do same with r and v to find axis limits
        self.axElectronA.set_xlim(t_lims)
        self.axElectronA.set_ylim(self.get_limits1(['r_mag'], ''))
        self.axElectronA.set_xlabel('t (s)')
        self.axElectronA.set_ylabel('position from origin (10^8m)', color='g')
        self.axElectronB.set_ylim(self.get_limits1(['v_mag'], ''))
        self.axElectronB.set_ylabel('velocity (10^8m/s)', color='r')

        self.axPhoton1A.set_xlim(t_lims)
        self.axPhoton1A.set_ylim(self.get_limits2(['r_mag'], ''))
        self.axPhoton1A.set_xlabel('t (s)')
        self.axPhoton1A.set_ylabel('position from origin (10^8m)', color='g')
        self.axPhoton1B.set_ylim(self.get_limits2(['v_mag'], ''))
        self.axPhoton1B.set_ylabel('velocity (10^8m/s)', color='r')

        self.axPhoton2A.set_xlim(t_lims)
        self.axPhoton2A.set_ylim(self.get_limits2(['r_mag'], ''))
        self.axPhoton2A.set_xlabel('t (s)')
        self.axPhoton2A.set_ylabel('position from origin (10^8m)', color='g')
        self.axPhoton2B.set_ylim(self.get_limits2(['v_mag'], ''))
        self.axPhoton2B.set_ylabel('velocity (10^8m/s)', color='r')

    def get_limits1(self, params, axis):
        lower_lim, upper_lim = 0, 0
        for p in params:
            m = max(self.simulation_results1['%s%s' % (p, axis)])
            if m > upper_lim:
                upper_lim = m
            m = min(self.simulation_results1['%s%s' % (p, axis)])
            if m < lower_lim:
                lower_lim = m
        return lower_lim - 0.05, upper_lim + 0.05

    def get_limits2(self, params, axis):
        lower_lim, upper_lim = 0, 0
        for p in params:
            m = max(self.simulation_results2['%s%s' % (p, axis)])
            if m > upper_lim:
                upper_lim = m
            m = min(self.simulation_results2['%s%s' % (p, axis)])
            if m < lower_lim:
                lower_lim = m
        return lower_lim - 0.05, upper_lim + 0.05

    def config_plots(self, electron_angle, photon_angle):
        #set titles
        self.ax1.set_title('Trajectory Visualisation\n Electron Recoil Angle: {} degrees     Photon Recoil Angle: {} degrees'.format(electron_angle, photon_angle))
        self.ax1.set_position([0, 0, 0.5, 1])
        self.ax1.set_aspect('auto')
        self.axElectronA.set_title('PINK - Position and Velocity vs Time of Electron', color='magenta', fontsize='10')
        self.axElectronA.grid()

        self.axPhoton1A.set_title('PURPLE - Position and Velocity vs Time of 1st Photon', color = 'purple', fontsize='10')
        self.axPhoton1A.grid()

        self.axPhoton2A.set_title('BLUE - Position and Velocity vs Time of 2nd Photon', color = 'blue', fontsize='10')
        self.axPhoton2A.grid()

    def visualize(self, i):
        # update trajectory of each particle for current time step
        self.trajectory1.set_data(self.simulation_results1['rx'][:i], self.simulation_results1['ry'][:i])
        self.trajectory1.set_3d_properties(self.simulation_results1['rz'][:i])

        self.trajectory2.set_data(self.simulation_results2['rx'][:i], self.simulation_results2['ry'][:i])
        self.trajectory2.set_3d_properties(self.simulation_results2['rz'][:i])

        self.trajectory3.set_data(self.simulation_results3['rx'][:i], self.simulation_results3['ry'][:i])
        self.trajectory3.set_3d_properties(self.simulation_results3['rz'][:i])

        time_stepe = self.simulation_results1['t'][:i]
        time_stepp = self.simulation_results2['t'][:i]

        #ELECTRON
        self.rvte.set_data(time_stepe, self.simulation_results1['r_mag'][:i]) #position vs time
        self.vvte.set_data(time_stepe, self.simulation_results1['v_mag'][:i]) # magnitude of velocity vs time

        #PHOTON 1
        self.rvtp1.set_data(time_stepp, self.simulation_results2['r_mag'][:i]) #position vs time
        self.vvtp1.set_data(time_stepp, self.simulation_results2['v_mag'][:i]) #position vs time

        #PHOTON 2
        self.rvtp2.set_data(time_stepp, self.simulation_results3['r_mag'][:i]) # magnitude of velocity vs time
        self.vvtp2.set_data(time_stepp, self.simulation_results3['v_mag'][:i]) # magnitude of velocity vs time

    def animate(self, time, electron_angle, photon_angle):
        return animation.FuncAnimation(self.fig,
                                       self.visualize,
                                       frames=len(time),
                                       init_func=self.config_plots(electron_angle, photon_angle),
                                       blit=False,
                                       repeat=False,
                                       interval=2)
