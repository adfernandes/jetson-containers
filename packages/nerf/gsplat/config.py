from jetson_containers import CUDA_ARCHITECTURES

def gsplat(version, requires=None, default=False):
    pkg = package.copy()

    if requires:
        pkg['requires'] = requires   

    pkg['name'] = f'gsplat:{version}'

    pkg['build_args'] = {
        'CUDAARCHS': ';'.join([str(x) for x in CUDA_ARCHITECTURES]),
        'GSPLAT_VERSION': version,
    }

    builder = pkg.copy()

    builder['name'] = f'gsplat:{version}-builder'
    builder['build_args'] = {**pkg['build_args'], **{'FORCE_BUILD': 'on'}}

    if default:
        pkg['alias'] = 'gsplat'
        builder['alias'] = 'gsplat:builder'

    return pkg, builder

package = [
    gsplat('1.3.0', default=True)
]