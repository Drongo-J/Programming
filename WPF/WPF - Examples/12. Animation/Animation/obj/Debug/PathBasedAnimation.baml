   M S B A M L   `   `   `  ????  	Animation"    Animation.PathBasedAnimation   5   	   R NWindowsBase, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      8x,http://schemas.microsoft.com/winfx/2006/xaml    5        ? Title$  PathBasedAnimation??5      $??381.6??6    $??521.6??6/    ? 	Resources 5         path E? IsClosed ?? Point ?? Size ?? SweepDirection??%?   &	        B? 5      .??5	      E?  . .??5
   
   ?? $ 100,200&?6   $ 15,10??6%   $ 	Clockwise=?62   6O   ?? 5   
   $ 400,50&?6   $	 5,5??6$   62   5   	   5      5       ? Triggers 5      :? 5       :? RoutedEvent$ Window.Loaded??6   [?5      ?? 5   
   .??5      ?? .??5      T?  ?? 
TargetName$ image??6'   	 ?? TargetProperty$	 (Canvas.Left)?5   '   
 T? PathGeometry#
 [  5   &    g? Duration$ 0:0:5D?5   '    g? RepeatBehavior$ Forever??68    T? Source$ X=?6Q   T? 5      $ image??6'   $	 (Canvas.Top)?5   '   #
 [  5   &   $ 0:0:5D?5   '   $ Forever??68   $ Y=?6Q   5      5      5      .??5!      ?? $??10q?6   .+?5"      F? 
???  ??$??1??6   #??[  6,   
 ?? Top$ 10??6I    ?? Left$ 10??6Y   5#      ?? 5$      -   5        $??image??5$      ??5%      H? 5&   
    H? Drawing 5'      ? 5(       ? Brush
 ??İ? ? Geometry 5)      ? 5*      .??5+      @?  @? Center$ 10,10&?6$    @? RadiusX$ 9Q?63    @? RadiusY$ 4Q?6?   @? 5,      $ 10,10&?6$   $ 4Q?63   $ 9Q?6?   5-      
 ? Pen 5/      >? 50       >? 	Thickness$ 1Q?6    >? Brush
 ?   ?6$   52      54      56      57      58      