classdef PIDBase < handle
    properties(SetAccess = private)
        kp;
        ki;
        kd;
        
        error_sum;
        error_prev;
    end
    
    methods(Access=public)
        function obj = PIDBase(kp, ki, kd)
            obj.kp = kp;
            obj.ki = ki;
            obj.kd = kd;
            
            obj.error_sum = 0;
            obj.error_prev = 0;
        end
        
        function Reset(obj)
            obj.error_sum = 0;
            obj.error_prev = 0;
        end
        
        function u = Step(obj, error)
            obj.error_sum = obj.error_sum + error;
            u = obj.kp * error + obj.ki * obj.error_sum + obj.kd * (error - obj.error_prev);
            obj.error_prev = error;
        end
    end
end
