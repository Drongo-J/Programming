   M S B A M L   `   `   `  ????  	Animation    Animation.AnimationPlayer   5   	   R NWindowsBase, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      8x,http://schemas.microsoft.com/winfx/2006/xaml    5        ? Title$  	Animation??5      $	??396??6   $??360.8??6$    ? Triggers 5      :? 5       :? 
SourceName$ cmdStart??6    :? RoutedEvent$ Button.Click??6+   .[?5   
   ?? -   5         ??Name$ fadeStoryboardBegin??5      .??5      ?? -   5         g?Name$ fadeStoryboard??5       g? 
SpeedRatio 5      ??  ?? ElementName$ sldSpeed?? ?? Path$ Value?.??5      W? 	 ?? 
TargetName$	 imgDay??5      
 ?? TargetProperty$
 Opacity?5       W? From$ 1X?5      	 W? To$ 0X?6    g? Duration$ 0:0:10D?6!   66   5      5      5   	   :? 5      $ cmdPause??6   $ Button.Click??6+   .[?5   
   ??  ?? BeginStoryboardName$ fadeStoryboardBegin??6   6F   5   	   :? 5      $ 	cmdResume??6   $ Button.Click??6,   .[?5   
   ?? $ fadeStoryboardBegin??6   6G   5   	   :? 5      $ cmdStop??6   $ Button.Click??6*   .[?5   
   ?? $ fadeStoryboardBegin??6   6E   5   	   :? 5      $ 	cmdMiddle??6   $ Button.Click??6,   .[?5    
   ?? $ fadeStoryboardBegin??6    ?? Offset$ 0:0:5h?5!      6*   5"   	    ? 	Resources 5$       ?? 
TargetType ?? Property ?? Value??%~   '??       ?? 5%      " ??6   .?5&      ??  ? ??$ 5q?6"   6.   ?? 5'       ? ??$ 1q?6!   6-   5(      5)      .??5+      ?  ? RowDefinitions 5,      ?? 5-      6   ?? 5.      $
??Auto ?6   6&   ?? 5/      $
??Auto ?6   6&   ?? 50      $
??Auto ?6   6&   ?? 51      $
??Auto ?6   6&   .+?53      ? .+?54      ?? $??	night.jpg??6   6#   ?? 55      -   5        $??imgDay??55      $??day.jpg??6   6/   56      ?? 58      $??1??6    ?? Orientation$ 
Horizontal=?6   $??Center=?67   $??5q?6T   .+?59      ?? -   5        $??cmdStart??59      .??6   Start6&   ?? 5:      -   5        $??cmdPause??5:      .??6   Pause6&   ?? 5;      -   5        $??	cmdResume??5;      .??6    Resume6(   ?? 5<      -   5        $??cmdStop??5<      .??6   Stop6$   ?? 5=      -   5        $??	cmdMiddle??5=      .??6    Move To Middle60   5>      ?? 5@      -	   5        $??lblTime??5@      $??2??6   $??Center=?6,   [[ stopped ]]6X   ? 5A      $??3??6   $??5q?6    ? ColumnDefinitions 5B      ?? 5C   
   $
??Auto ?6   6*   ?? 5D   
   6   .+?5F      ?? Speed:6   ?? 5G      -
   5        $??sldSpeed??5G      $??1??6    ? Minimum$ 0Q?5H       ? Maximum$ 3Q?6    ? Value$ 1Q?6'    ?? TickPlacement$ BottomRight=?61    ?? TickFrequency$	 0.1Q?6M   5I   6   5J      ? 5K      -   5        $??progressBar??5K   =   $??4??6   $??0,5,0,0q?6   $??10??60   $ 0Q?6P   $ 1Q?6\   6j   5L      5M      