   M S B A M L   `   `   `  ????  DataBinding"    DataBinding.MultipleBindings   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5      R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5        ? Title$  MultipleBindings??5      $	??300??6   $	??300??6+   .??5      ? $??5q?6	    ? RowDefinitions 5      ?? 5	      $
??Auto ?6   6&   ?? 5
      $
??Auto ?6   6&   ?? 5      $
??Auto ?6   6&   ?? 5      $
??Auto ?6   6&   ?? 5      6   .+?5      ?? -   5        $??sliderFontSize??5      $??3q?6#    ? Minimum$ 1Q?6.    ? Maximum$ 40Q?6:    ? Value$ 10Q?6G   6T   ?? 5      -   5        $??
txtContent??5      $??3q?6    $??2??6+   .??68   Sample Content6H   ?? 5      -   5        $??	lstColors??5   &   $??3q?6   $??3??6   .@?5      ?? 
 ? Tag$
 Blue??6   .??6   Blue6%   ?? 5      $ DarkBlue??6   .??6#   	Dark Blue6.   ?? 5      $ 	LightBlue??6   .??6$   
Light Blue60   5      ?? 5      -   5        $??lblSampleText??5      $??3q?6   $??4??5   I   ??6   ??  ?? ElementName$ sliderFontSize?? ?? Path$ Value???5      ?? $ 
txtContent??$
 Text???5      ?? $ 	lstColors??$ SelectedItem.Tag?5      5!      5"      