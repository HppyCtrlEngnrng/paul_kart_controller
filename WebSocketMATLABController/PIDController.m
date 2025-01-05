classdef PIDController < handle
    properties(SetAccess = private)
        pid_x;
        pid_y;
        pid_z;
        
        input_gain_x;
        input_gain_y;
        input_gain_z;
    end
    
    methods(Access=public)
        function obj = PIDController(kp_x, ki_x, kd_x, kp_y, ki_y, kd_y, kp_z, ki_z, kd_z, input_gain_x, input_gain_y, input_gain_z)
            obj.pid_x = PIDBase(kp_x, ki_x, kd_x);
            obj.pid_y = PIDBase(kp_y, ki_y, kd_y);
            obj.pid_z = PIDBase(kp_z, ki_z, kd_z);
            
            obj.input_gain_x = input_gain_x;
            obj.input_gain_y = input_gain_y;
            obj.input_gain_z = input_gain_z;
        end
        
        function [u_x, u_y, u_z] = Step(obj, reset_flag, angle_x, ang_vel_y, angle_z, input_x, input_y, input_z)
            if reset_flag
                obj.Reset();
            end
            
            u_x = obj.pid_x.Step(angle_x) + obj.input_gain_x * input_x;
            u_y = obj.pid_y.Step(obj.input_gain_y * input_y - ang_vel_y);
            u_z = obj.pid_z.Step(angle_z) + obj.input_gain_z * input_z;
        end
        
        function Reset(obj)
            obj.pid_x.Reset();
            obj.pid_y.Reset();
            obj.pid_z.Reset();
        end
    end
end
