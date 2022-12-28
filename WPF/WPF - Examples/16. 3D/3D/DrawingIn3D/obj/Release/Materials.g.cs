﻿#pragma checksum "..\..\Materials.xaml" "{8829d00f-11b8-4213-878b-770e8597ac16}" "4DA56DCF5B188F40D255423666ECD4A8BFBCF0F86A5CAD2DDF07DF120A29F18C"
//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Automation;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Ink;
using System.Windows.Input;
using System.Windows.Markup;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Effects;
using System.Windows.Media.Imaging;
using System.Windows.Media.Media3D;
using System.Windows.Media.TextFormatting;
using System.Windows.Navigation;
using System.Windows.Shapes;


namespace DrawingIn3D {
    
    
    /// <summary>
    /// Materials
    /// </summary>
    public partial class Materials : System.Windows.Window, System.Windows.Markup.IComponentConnector {
        
        
        #line 26 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.CheckBox chkBackground;
        
        #line default
        #line hidden
        
        
        #line 27 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.CheckBox chkDiffuse;
        
        #line default
        #line hidden
        
        
        #line 28 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.CheckBox chkSpecular;
        
        #line default
        #line hidden
        
        
        #line 29 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.CheckBox chkEmissive;
        
        #line default
        #line hidden
        
        
        #line 33 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Shapes.Rectangle rect;
        
        #line default
        #line hidden
        
        
        #line 36 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.PerspectiveCamera camera;
        
        #line default
        #line hidden
        
        
        #line 43 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.Model3DGroup Scene;
        
        #line default
        #line hidden
        
        
        #line 50 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.Model3DGroup ring;
        
        #line default
        #line hidden
        
        
        #line 65 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.GeometryModel3D Torus01OR9GR10;
        
        #line default
        #line hidden
        
        
        #line 67 "..\..\Materials.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.MaterialGroup materialsGroup;
        
        #line default
        #line hidden
        
        private bool _contentLoaded;
        
        /// <summary>
        /// InitializeComponent
        /// </summary>
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        public void InitializeComponent() {
            if (_contentLoaded) {
                return;
            }
            _contentLoaded = true;
            System.Uri resourceLocater = new System.Uri("/DrawingIn3D;component/materials.xaml", System.UriKind.Relative);
            
            #line 1 "..\..\Materials.xaml"
            System.Windows.Application.LoadComponent(this, resourceLocater);
            
            #line default
            #line hidden
        }
        
        [System.Diagnostics.DebuggerNonUserCodeAttribute()]
        [System.CodeDom.Compiler.GeneratedCodeAttribute("PresentationBuildTasks", "4.0.0.0")]
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Never)]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Design", "CA1033:InterfaceMethodsShouldBeCallableByChildTypes")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Maintainability", "CA1502:AvoidExcessiveComplexity")]
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1800:DoNotCastUnnecessarily")]
        void System.Windows.Markup.IComponentConnector.Connect(int connectionId, object target) {
            switch (connectionId)
            {
            case 1:
            
            #line 25 "..\..\Materials.xaml"
            ((System.Windows.Controls.StackPanel)(target)).AddHandler(System.Windows.Controls.Primitives.ButtonBase.ClickEvent, new System.Windows.RoutedEventHandler(this.chk_Click));
            
            #line default
            #line hidden
            return;
            case 2:
            this.chkBackground = ((System.Windows.Controls.CheckBox)(target));
            return;
            case 3:
            this.chkDiffuse = ((System.Windows.Controls.CheckBox)(target));
            return;
            case 4:
            this.chkSpecular = ((System.Windows.Controls.CheckBox)(target));
            return;
            case 5:
            this.chkEmissive = ((System.Windows.Controls.CheckBox)(target));
            return;
            case 6:
            this.rect = ((System.Windows.Shapes.Rectangle)(target));
            return;
            case 7:
            this.camera = ((System.Windows.Media.Media3D.PerspectiveCamera)(target));
            return;
            case 8:
            this.Scene = ((System.Windows.Media.Media3D.Model3DGroup)(target));
            return;
            case 9:
            this.ring = ((System.Windows.Media.Media3D.Model3DGroup)(target));
            return;
            case 10:
            this.Torus01OR9GR10 = ((System.Windows.Media.Media3D.GeometryModel3D)(target));
            return;
            case 11:
            this.materialsGroup = ((System.Windows.Media.Media3D.MaterialGroup)(target));
            return;
            }
            this._contentLoaded = true;
        }
    }
}
