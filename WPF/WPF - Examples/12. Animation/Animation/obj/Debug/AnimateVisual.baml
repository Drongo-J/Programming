   M S B A M L   `   `   `  ????  	Animation    Animation.AnimateVisual   5   	   R NWindowsBase, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      8x,http://schemas.microsoft.com/winfx/2006/xaml    5        ? Title$  AnimateVisualBrush??5      $	??300??6    $	??300??6-   
???????.??5      ?  ? RowDefinitions 5      ?? 5   
   6   ?? 5	   
   6   .+?5      ?? -   5        $??visual??5      $??Center=?6   $??Center=?6:   $
??Test??5   .    ? Triggers 5   
   :? 5       :? RoutedEvent$ Button.Click??6   .[?5      ?? .??5      ??  g? RepeatBehavior$ Forever??6   .??5      W?  ?? 
TargetName$ 	rectangle??6"    ?? TargetProperty$( "RenderTransform.Children[0].AngleY?5   "   	 W? To$	 180X?5   "    g? Duration$ 0:0:15D?6+   	 g? AutoReverse	 . 6R   W? 5      $ 	rectangle??6"   $' !RenderTransform.Children[1].Angle?5   "   $	 180X?5   "   $ 0:0:20D?6+   	 . 6R   W? 5      $ 	rectangle??6"   $ Opacity?5   "   $	 0.1X?5   "   $ 0:0:4D?6+   	 . 6Q   5      5      5      5   	   ?? 5!      -   5        $??	rectangle??5!      $??1??6   $	??100??60   
 ?? Stretch$
 Uniform=?6<   }?.   J? RenderTransformOrigin$ 0.5,0.5&?6c   ??5"   
   !? 5#       !? Visual 6   ??  ?? ElementName$ visual??5%      z?5'   
   V? 5)      .~?5*      ??  ?? CenterX$	 0.5Q?6   6.   ?? 5+       ?? CenterX$	 0.5Q?6     ?? CenterY$	 0.5Q?6.   6>   5,      5/   	   50      51      