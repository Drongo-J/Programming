   M S B A M L   `   `   `  ????  SoundAndVideo'    !SoundAndVideo.DeclarativePlayback   5   	   R NWindowsBase, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      8x,http://schemas.microsoft.com/winfx/2006/xaml    5        ? Title$  DeclarativePlayback??5      $??234.4??6!   $	??304??60    ? 	Resources 5         MediaStoryboardResource I? SlipBehavior ?? 
TargetName p? Source g? FillBehavior??%?   &	        ?? 5
      $
 Slip=?63   .??5      p? $ media??6   $ test.mp3??64   $ HoldEnd=?6F   5      5   	   5      .??5      ? $??5q?6    ? RowDefinitions 5      ?? 5   
   $
??Auto ?6   6(   ?? 5   
   $
??Auto ?6   6(    ? Triggers 5   
   :? 5       :? RoutedEvent$ ButtonBase.Click??6   	 :? 
SourceName$	 cmdPlay??6:   [?5      ?? 5      -   5        
 ??Name$
 MediaStoryboard??5   "   #??[  69   5      :? 5      $ ButtonBase.Click??6   $	 cmdStop??6:   [?5      ?? 5        ?? BeginStoryboardName$ MediaStoryboard??6!   5"      :? 5#      $ ButtonBase.Click??6   $	 cmdPause??6:   [?5$      ?? 5%      $ MediaStoryboard??6"   5'      :? 5(      $ ButtonBase.Click??6   $	 	cmdResume??6:   [?5)      ?? 5*      $ MediaStoryboard??6#   5,      .+?5/      r? -   5        $??media??5/      6$   ?? 50       ?? Orientation$ 
Horizontal=?6   .+?51   
   ?? -   5        $??cmdPlay??51      $??5q?6    $??1q?6,   .??67   Play6=   ?? 52   
   -   5        $??cmdStop??52      $??5q?6    $??1q?6,   .??67   Stop6=   ?? 53   
   -   5        $??cmdPause??53      $??5q?6!   $??1q?6-   .??68   Pause6?   ?? 54   
   -   5        $??	cmdResume??54      $??5q?6"   $??1q?6.   .??69   Resume6A   55      ? 57      $??0,10,0,0q?6   $??2??6    58   
   ?? 59      $
??Auto ?6   6*   ?? 5:      $
??Auto ?6   6*    ? ColumnDefinitions 5<   
   ?? 5=      $
??Auto ?6   6,   ?? 5>      6   .+?5@   
   ?? $??5q?6   	Volume:6)   ?? 5A   
   $??1??6    ? Minimum$ 0Q?6!    ? Maximum$ 1Q?6-    ? Value 5B      ??  ?? ElementName$ media?? ?? Path$ Volume? ?? Mode$ TwoWay=?6O   ?? 5C   
   $??5q?6   $??1??6   
Balance:67   ?? 5D      $??1??6   $??1??6   $ -1Q?6,   $ 1Q?69    5E   	   ?? $ media??$ Balance?$ TwoWay=?6J   5F   	   5G      5I      