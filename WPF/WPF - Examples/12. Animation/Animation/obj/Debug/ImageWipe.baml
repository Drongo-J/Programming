   M S B A M L   `   `   `  ????  	Animation    Animation.ImageWipe   5   	   R NWindowsBase, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      8x,http://schemas.microsoft.com/winfx/2006/xaml    5        ? Title$  	ImageWipe??5      $	??300??6   $	??300??6$   .??5      ?  ? RowDefinitions 5      ?? 5	      6   ?? 5
      $
??Auto ?6   6&   .+?5      ? .+?5      ?? $??	night.jpg??6   6#   ?? 5      -   5        $??imgDay??5      $??day.jpg??6    J? OpacityMask 5   
   ?? 5       ?? 
StartPoint$	 0,0&?6     ?? EndPoint$	 1,0&?61   .??5      ?  ? Offset$ 0Q?6    ? Color$ Transparent??6&   -   5        transparentStop??5   :   ? 5      $ 0Q?6   $ Black??6&   -   5        visibleStop??5   4   5      5   	   5      ?? 5      -   5        $??cmdStart??5      $??1??6   $??5q?6,   $??5q?68   .??6C   Start ? Triggers 5   
   :? 5       :? 
SourceName$ cmdStart??6   	 :? RoutedEvent$	 Button.Click??6/   .[?5      ?? .??5      ?? .??5      W? 
 ?? 
TargetName$
 transparentStop??5        ?? TargetProperty$ Offset?5!       g? 	BeginTime$ 0:0:0.2X?68    W? From$ 0X?5"      	 W? To$ 1X?6    g? Duration$ 0:0:1D?6%   69   W? 5#      $
 visibleStop??5$      $ Offset?5%      $ 0X?5&      $	 1.2X?6   $ 0:0:1.2D?6'   6=   5'      5(      5)      5,   	   51      52      