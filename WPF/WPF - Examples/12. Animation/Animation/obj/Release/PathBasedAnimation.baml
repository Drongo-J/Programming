   M S B A M L   `   `   `  ????   	Animation"    Animation.PathBasedAnimation   R NWindowsBase, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    8x,http://schemas.microsoft.com/winfx/2006/xaml      ? Title$  PathBasedAnimation??$??381.6??$??521.6?? ? 	Resources    path E? IsClosed ?? Point ?? Size ?? SweepDirection??%l   &	        B? .??E?  . .???? $ 100,200&?$ 15,10??$ 	Clockwise=??? $ 400,50&?$	 5,5?? ? Triggers :?  :? RoutedEvent$ Window.Loaded??[??? .???? .??T?  ?? 
TargetName$ image??	 ?? TargetProperty$	 (Canvas.Left)?
 T? PathGeometry#
 [   g? Duration$ 0:0:5D? g? RepeatBehavior$ Forever?? T? Source$ X=?T? $ image??$	 (Canvas.Top)?#
 [  $ 0:0:5D?$ Forever??$ Y=?.???? $??10q?.+?F? 
???  ??$??1??#??[  
 ?? Top$ 10?? ?? Left$ 10???? -   $??image????H?  H? Drawing ?  ? Brush
 ??İ? ? Geometry ? .??@?  @? Center$ 10,10&? @? RadiusX$ 9Q? @? RadiusY$ 4Q?@? $ 10,10&?$ 4Q?$ 9Q?
 ? Pen >?  >? 	Thickness$ 1Q? >? Brush
 ?   ?