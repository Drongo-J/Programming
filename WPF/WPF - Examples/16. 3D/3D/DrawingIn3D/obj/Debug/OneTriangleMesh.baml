   M S B A M L   `   `   `  ????I  E3DTools, Version=1.0.8369.23443, Culture=neutral, PublicKeyToken=null4'clr-namespace:_3DTools;assembly=3DTools_3DTools  5   	    DrawingIn3D!   DrawingIn3D.OneTriangleMesh   5   	   \ XPresentationFramework, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      8x,http://schemas.microsoft.com/winfx/2006/xaml    5      7tools'clr-namespace:_3DTools;assembly=3DTools    5   	     ? Title$  OneTriangleMesh??5      $	??300??6   $	??300??6*   .??5      ? $??5q?6   .+?5      ?? 
??? ???$??1q?6$   ._?5	      '?  '? Camera 5
   
   =? 5       ? Position$ -2,2,21?5       ? LookDirection$ 2,-2,-25?5       ? UpDirection$ 0,1,05?5      .x?5   
   g?  g? Content 5      t? 5       ?? Color$ White??5       t? 	Direction$ -1,-1,-15?5      5      g? 5   
    5      ? 5       ? Geometry 5      k? 5      	 k? 	Positions	 ?   
 k? TriangleIndices
 ?    5   !    ? Material 5!      u? 5"       u? Brush
 ? ???6"   5)      5+      !   _3DTools.ScreenSpaceLines3D  5-   
      Points ?   ?ig????    	Thickness$ 1Q?5.         Color$
 Blue??6   5/        50   
    ?   ?ig???? $ 1Q?51      $	 Red??6   52        53   
    ?   ?ig???? $ 1Q?54      $ Green??6   55      56   	   57   	   58      59      