﻿#pragma checksum "..\..\HitTesting.xaml" "{8829d00f-11b8-4213-878b-770e8597ac16}" "E2820C25F7AD12569B488D783FD6AF9D7AC48DD796D9A37B53A92CE4DBB04335"
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
using _3DTools;


namespace DrawingIn3D {
    
    
    /// <summary>
    /// HitTesting
    /// </summary>
    public partial class HitTesting : System.Windows.Window, System.Windows.Markup.IComponentConnector {
        
        
        #line 11 "..\..\HitTesting.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Controls.Viewport3D viewport;
        
        #line default
        #line hidden
        
        
        #line 13 "..\..\HitTesting.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.PerspectiveCamera camera;
        
        #line default
        #line hidden
        
        
        #line 16 "..\..\HitTesting.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.ModelUIElement3D ringVisual;
        
        #line default
        #line hidden
        
        
        #line 19 "..\..\HitTesting.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.Model3DGroup Scene;
        
        #line default
        #line hidden
        
        
        #line 40 "..\..\HitTesting.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.GeometryModel3D ringModel;
        
        #line default
        #line hidden
        
        
        #line 72 "..\..\HitTesting.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.MeshGeometry3D ringMesh;
        
        #line default
        #line hidden
        
        
        #line 81 "..\..\HitTesting.xaml"
        [System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
        internal System.Windows.Media.Media3D.AxisAngleRotation3D axisRotation;
        
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
            System.Uri resourceLocater = new System.Uri("/DrawingIn3D;component/hittesting.xaml", System.UriKind.Relative);
            
            #line 1 "..\..\HitTesting.xaml"
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
            this.viewport = ((System.Windows.Controls.Viewport3D)(target));
            return;
            case 2:
            this.camera = ((System.Windows.Media.Media3D.PerspectiveCamera)(target));
            return;
            case 3:
            this.ringVisual = ((System.Windows.Media.Media3D.ModelUIElement3D)(target));
            
            #line 16 "..\..\HitTesting.xaml"
            this.ringVisual.MouseDown += new System.Windows.Input.MouseButtonEventHandler(this.ringVisual_MouseDown);
            
            #line default
            #line hidden
            return;
            case 4:
            this.Scene = ((System.Windows.Media.Media3D.Model3DGroup)(target));
            return;
            case 5:
            this.ringModel = ((System.Windows.Media.Media3D.GeometryModel3D)(target));
            return;
            case 6:
            this.ringMesh = ((System.Windows.Media.Media3D.MeshGeometry3D)(target));
            return;
            case 7:
            this.axisRotation = ((System.Windows.Media.Media3D.AxisAngleRotation3D)(target));
            return;
            }
            this._contentLoaded = true;
        }
    }
}

