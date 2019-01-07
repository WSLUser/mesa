#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mesa
Version  : 1
Release  : 176
URL      : https://cgit.freedesktop.org/mesa/mesa/snapshot/1e872d14865fbe8dddf41b57b79137305144ead1.tar.gz
Source0  : https://cgit.freedesktop.org/mesa/mesa/snapshot/1e872d14865fbe8dddf41b57b79137305144ead1.tar.gz
Summary  : Mesa Off-screen Rendering library
Group    : Development/Tools
License  : MIT
Requires: mesa-data = %{version}-%{release}
Requires: mesa-lib = %{version}-%{release}
Requires: mesa-license = %{version}-%{release}
BuildRequires : Mako-legacypython
BuildRequires : Mako-python
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Loader-dev32
BuildRequires : Vulkan-Tools
BuildRequires : bison
BuildRequires : buildreq-meson
BuildRequires : buildreq-scons
BuildRequires : elfutils-dev
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : grep
BuildRequires : libgcrypt-dev
BuildRequires : libpthread-stubs-dev
BuildRequires : llvm-dev
BuildRequires : nettle-dev
BuildRequires : nettle-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32dri2proto)
BuildRequires : pkgconfig(32dri3proto)
BuildRequires : pkgconfig(32expat)
BuildRequires : pkgconfig(32glproto)
BuildRequires : pkgconfig(32libdrm)
BuildRequires : pkgconfig(32libdrm_amdgpu)
BuildRequires : pkgconfig(32libdrm_intel)
BuildRequires : pkgconfig(32pthread-stubs)
BuildRequires : pkgconfig(32wayland-egl-backend)
BuildRequires : pkgconfig(32wayland-protocols)
BuildRequires : pkgconfig(32wayland-server)
BuildRequires : pkgconfig(32x11-xcb)
BuildRequires : pkgconfig(32xcb)
BuildRequires : pkgconfig(32xcb-dri2)
BuildRequires : pkgconfig(32xcb-xfixes)
BuildRequires : pkgconfig(32xdamage)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xfixes)
BuildRequires : pkgconfig(32xrandr)
BuildRequires : pkgconfig(32xshmfence)
BuildRequires : pkgconfig(32xvmc)
BuildRequires : pkgconfig(32xxf86vm)
BuildRequires : pkgconfig(32zlib)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(glproto)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_amdgpu)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(presentproto)
BuildRequires : pkgconfig(pthread-stubs)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(wayland-egl-backend)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-dri2)
BuildRequires : pkgconfig(xcb-xfixes)
BuildRequires : pkgconfig(xdamage)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : pkgconfig(xvmc)
BuildRequires : pkgconfig(xxf86vm)
BuildRequires : pkgconfig(zlib)
BuildRequires : sed
BuildRequires : wayland-dev
BuildRequires : wayland-dev32
BuildRequires : wayland-protocols-dev
Patch1: build.patch
Patch2: avx2-drivers.patch
Patch3: gnu11.patch

%description
This local copy of a SHA1 implementation based on the sources below.
Why:
- Some libraries suffer from race condition and other issues. For example see
commit ade3108bb5b0 ("util: Fix race condition on libgcrypt initialization").

%package data
Summary: data components for the mesa package.
Group: Data

%description data
data components for the mesa package.


%package dev
Summary: dev components for the mesa package.
Group: Development
Requires: mesa-lib = %{version}-%{release}
Requires: mesa-data = %{version}-%{release}
Provides: mesa-devel = %{version}-%{release}

%description dev
dev components for the mesa package.


%package dev32
Summary: dev32 components for the mesa package.
Group: Default
Requires: mesa-lib32 = %{version}-%{release}
Requires: mesa-data = %{version}-%{release}
Requires: mesa-dev = %{version}-%{release}

%description dev32
dev32 components for the mesa package.


%package lib
Summary: lib components for the mesa package.
Group: Libraries
Requires: mesa-data = %{version}-%{release}
Requires: mesa-license = %{version}-%{release}

%description lib
lib components for the mesa package.


%package lib32
Summary: lib32 components for the mesa package.
Group: Default
Requires: mesa-data = %{version}-%{release}
Requires: mesa-license = %{version}-%{release}

%description lib32
lib32 components for the mesa package.


%package license
Summary: license components for the mesa package.
Group: Default

%description license
license components for the mesa package.


%prep
%setup -q -n 1e872d14865fbe8dddf41b57b79137305144ead1
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a 1e872d14865fbe8dddf41b57b79137305144ead1 build32
popd
pushd ..
cp -a 1e872d14865fbe8dddf41b57b79137305144ead1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545427282
unset LD_AS_NEEDED
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%reconfigure --disable-static --enable-dri \
--enable-dri3 \
--enable-glx \
--enable-gles2 \
--enable-xorg \
--enable-shared-glapi \
--enable-xorg \
--enable-glx-tls \
--enable-xvmc \
--enable-glx-tls \
--enable-texture-float \
--enable-gbm \
--enable-llvm \
--disable-omx-tizonia \
--disable-omx-bellagio \
--sysconfdir=/usr/share/mesa \
--with-egl-platforms=x11,drm,wayland \
--with-vulkan-drivers=intel,radeon --with-gallium-drivers="radeonsi,r600,nouveau,svga,swrast" --enable-gallium-osmesa
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="$ASFLAGS --32"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static --enable-dri \
--enable-dri3 \
--enable-glx \
--enable-gles2 \
--enable-xorg \
--enable-shared-glapi \
--enable-xorg \
--enable-glx-tls \
--enable-xvmc \
--enable-glx-tls \
--enable-texture-float \
--enable-gbm \
--enable-llvm \
--disable-omx-tizonia \
--disable-omx-bellagio \
--sysconfdir=/usr/share/mesa \
--with-egl-platforms=x11,drm,wayland \
--with-vulkan-drivers=intel,radeon --disable-va \
--with-dri-drivers="i965" \
--without-gallium-drivers \
--disable-gallium-llvm \
--disable-llvm \
--with-vulkan-drivers=intel --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%reconfigure --disable-static --enable-dri \
--enable-dri3 \
--enable-glx \
--enable-gles2 \
--enable-xorg \
--enable-shared-glapi \
--enable-xorg \
--enable-glx-tls \
--enable-xvmc \
--enable-glx-tls \
--enable-texture-float \
--enable-gbm \
--enable-llvm \
--disable-omx-tizonia \
--disable-omx-bellagio \
--sysconfdir=/usr/share/mesa \
--with-egl-platforms=x11,drm,wayland \
--with-vulkan-drivers=intel,radeon
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1545427282
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mesa
cp docs/license.html %{buildroot}/usr/share/package-licenses/mesa/docs_license.html
cp src/intel/tools/imgui/LICENSE.txt %{buildroot}/usr/share/package-licenses/mesa/src_intel_tools_imgui_LICENSE.txt
cp src/mapi/glapi/gen/license.py %{buildroot}/usr/share/package-licenses/mesa/src_mapi_glapi_gen_license.py
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
## install_append content
mv %{buildroot}/usr/lib64/dri/haswell/i965_dri.so %{buildroot}/usr/lib64/dri/i965_dri.so.avx2
rm -rf  %{buildroot}/usr/lib64/haswell
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/drirc.d/00-mesa-defaults.conf
/usr/share/vulkan/icd.d/intel_icd.i686.json
/usr/share/vulkan/icd.d/intel_icd.x86_64.json
/usr/share/vulkan/icd.d/radeon_icd.x86_64.json

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/EGL/egl.h
/usr/include/EGL/eglext.h
/usr/include/EGL/eglextchromium.h
/usr/include/EGL/eglmesaext.h
/usr/include/EGL/eglplatform.h
/usr/include/GL/gl.h
/usr/include/GL/gl_mangle.h
/usr/include/GL/glcorearb.h
/usr/include/GL/glext.h
/usr/include/GL/glx.h
/usr/include/GL/glx_mangle.h
/usr/include/GL/glxext.h
/usr/include/GL/internal/dri_interface.h
/usr/include/GL/osmesa.h
/usr/include/GLES/egl.h
/usr/include/GLES/gl.h
/usr/include/GLES/glext.h
/usr/include/GLES/glplatform.h
/usr/include/GLES2/gl2.h
/usr/include/GLES2/gl2ext.h
/usr/include/GLES2/gl2platform.h
/usr/include/GLES3/gl3.h
/usr/include/GLES3/gl31.h
/usr/include/GLES3/gl32.h
/usr/include/GLES3/gl3ext.h
/usr/include/GLES3/gl3platform.h
/usr/include/KHR/khrplatform.h
/usr/include/vulkan/vulkan_intel.h
/usr/lib64/pkgconfig/dri.pc
/usr/lib64/pkgconfig/egl.pc
/usr/lib64/pkgconfig/gbm.pc
/usr/lib64/pkgconfig/gl.pc
/usr/lib64/pkgconfig/glesv1_cm.pc
/usr/lib64/pkgconfig/glesv2.pc
/usr/lib64/pkgconfig/osmesa.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32dri.pc
/usr/lib32/pkgconfig/32egl.pc
/usr/lib32/pkgconfig/32gbm.pc
/usr/lib32/pkgconfig/32gl.pc
/usr/lib32/pkgconfig/32glesv1_cm.pc
/usr/lib32/pkgconfig/32glesv2.pc
/usr/lib32/pkgconfig/dri.pc
/usr/lib32/pkgconfig/egl.pc
/usr/lib32/pkgconfig/gbm.pc
/usr/lib32/pkgconfig/gl.pc
/usr/lib32/pkgconfig/glesv1_cm.pc
/usr/lib32/pkgconfig/glesv2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/dri/haswell/i915_dri.so
/usr/lib64/dri/haswell/kms_swrast_dri.so
/usr/lib64/dri/haswell/nouveau_vieux_dri.so
/usr/lib64/dri/haswell/r200_dri.so
/usr/lib64/dri/haswell/r300_dri.so
/usr/lib64/dri/haswell/r600_dri.so
/usr/lib64/dri/haswell/radeon_dri.so
/usr/lib64/dri/haswell/swrast_dri.so
/usr/lib64/dri/haswell/vmwgfx_dri.so
/usr/lib64/dri/i915_dri.so
/usr/lib64/dri/i965_dri.so
/usr/lib64/dri/i965_dri.so.avx2
/usr/lib64/dri/kms_swrast_dri.so
/usr/lib64/dri/nouveau_dri.so
/usr/lib64/dri/nouveau_vieux_dri.so
/usr/lib64/dri/r200_dri.so
/usr/lib64/dri/r600_dri.so
/usr/lib64/dri/radeon_dri.so
/usr/lib64/dri/radeonsi_dri.so
/usr/lib64/dri/swrast_dri.so
/usr/lib64/dri/vmwgfx_dri.so
/usr/lib64/libEGL.so
/usr/lib64/libEGL.so.1
/usr/lib64/libEGL.so.1.0.0
/usr/lib64/libGL.so
/usr/lib64/libGL.so.1
/usr/lib64/libGL.so.1.2.0
/usr/lib64/libGLESv1_CM.so
/usr/lib64/libGLESv1_CM.so.1
/usr/lib64/libGLESv1_CM.so.1.1.0
/usr/lib64/libGLESv2.so
/usr/lib64/libGLESv2.so.2
/usr/lib64/libGLESv2.so.2.0.0
/usr/lib64/libOSMesa.so
/usr/lib64/libOSMesa.so.8
/usr/lib64/libOSMesa.so.8.0.0
/usr/lib64/libXvMCnouveau.so
/usr/lib64/libXvMCnouveau.so.1
/usr/lib64/libXvMCnouveau.so.1.0
/usr/lib64/libXvMCnouveau.so.1.0.0
/usr/lib64/libXvMCr600.so
/usr/lib64/libXvMCr600.so.1
/usr/lib64/libXvMCr600.so.1.0
/usr/lib64/libXvMCr600.so.1.0.0
/usr/lib64/libgbm.so
/usr/lib64/libgbm.so.1
/usr/lib64/libgbm.so.1.0.0
/usr/lib64/libglapi.so
/usr/lib64/libglapi.so.0
/usr/lib64/libglapi.so.0.0.0
/usr/lib64/libvulkan_intel.so
/usr/lib64/libvulkan_radeon.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/dri/i965_dri.so
/usr/lib32/libEGL.so
/usr/lib32/libEGL.so.1
/usr/lib32/libEGL.so.1.0.0
/usr/lib32/libGL.so
/usr/lib32/libGL.so.1
/usr/lib32/libGL.so.1.2.0
/usr/lib32/libGLESv1_CM.so
/usr/lib32/libGLESv1_CM.so.1
/usr/lib32/libGLESv1_CM.so.1.1.0
/usr/lib32/libGLESv2.so
/usr/lib32/libGLESv2.so.2
/usr/lib32/libGLESv2.so.2.0.0
/usr/lib32/libgbm.so
/usr/lib32/libgbm.so.1
/usr/lib32/libgbm.so.1.0.0
/usr/lib32/libglapi.so
/usr/lib32/libglapi.so.0
/usr/lib32/libglapi.so.0.0.0
/usr/lib32/libvulkan_intel.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mesa/docs_license.html
/usr/share/package-licenses/mesa/src_intel_tools_imgui_LICENSE.txt
/usr/share/package-licenses/mesa/src_mapi_glapi_gen_license.py
