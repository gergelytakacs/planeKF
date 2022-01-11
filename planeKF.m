% Gergely Takacs, 2022
%
% MATLAB realization of the KF example explained
% by Michel van Biezen in his lecture series on 
% the Kalman filter. See https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT
% for the full lecture series. The example starts at Lecture 27, i.e.
% https://www.youtube.com/playlist?list=PLX2gX-ftPVXU3oUFNATxGXY90AULiqnWT
%
% WARNING: Do not implement the Pp=diag(diag(Pp)) line outside
% this educational example. This is only to make the hand calculation
% demonstrated easier.

% Given (initial conditions
a=2;         % (m/s^2) Acceleration (constant)
T=1;         % (s) Sampling time
x0 = 4000;   % (m) Position init. cond.
v0 = 280;    % (m/s) Velocity init. cond.
x=[x0;v0];   % Estimated state vector (to store results)
Xp=[];       % Initialization just for storing predictions later

% Observations (measurements)
xo = [4000 4260 4550 4860 5110]; % (m) Position observation
vo = [280  282  285  286  290];  % (m/s) Velocity observation
xo = [xo; vo];                   % Observed states

% Initial state error covariance matrix
dPx = 20; % (m)   Variance guess in position
dPy = 5;  % (m/s) Variance giess in velocity
P= diag([dPx^2,dPy^2]);  % Initial estimate for state error covariance matrix

% Process noise
Q=zeros(2); % No process noise assumed

%Observation errors
dx = 25; % (m)   Error in position measurement
dy = 6; % (m/s) Error in velocity measurement
R=diag([dx^2, dy^2]); % Process noise covariance matrix

% State-space formulation
A=[1 T; 0 1];   % State transition matrix
B=[1/2*T^2 T]'; % Input matrix
C=eye(2);       % Measurement matrix
H=eye(2);       % Measurement to state transformatio 

%% Filter in action
run=4
for i=1:1:run
    
disp(['Iteration:',num2str(i)])
% Prediction part (p)
xp=A*x(:,i)+B*a % Predict state
Pp=A*P*A'+Q     % Predict state covariance
% SIMPLIFICATION FOR HAND CALCULATION, DO NOT USE IN REAL ALGORITHM
Pp=diag(diag(Pp)) % Comment out! Leaves out off-diagonals

% Update part
K=Pp*H'*inv(H*Pp*H'+R) % Kalman gain
y=C*xo(:,i+1)             % New observation
x(:,i+1)=xp+K*(y-H*xp)    % Updated state (current state)
P=(eye(2)-K*H)*Pp         % Uptated state covariance

% Plotting
Xp=[Xp,xp];        % Store predicted state, just for visualization
subplot(1,2,1)            
plot(xo(1,1:i),'-o')
hold on
plot([x0 Xp(1,1:i-1)],'-x')
plot(x(1,1:i),'-^')
hold off
legend('Observation','Prediction','KF')
xlabel('Time (s)')
ylabel('Position (m)')

subplot(1,2,2)            
plot(xo(2,1:i),'-o')
hold on
plot([v0 Xp(2,1:i-1)],'-x')
plot(x(2,1:i),'-^')
hold off
legend('Observation','Prediction','KF')
xlabel('Time (s)')
ylabel('Velocity (m/s)')

pause
end
