{
    "targets": [{
        "target_name": "mmap-io",
        "sources": [ "src/mmap-io.cc" ],
        "include_dirs": [
            "<!(node -e \"require('nan')\")"
        ],
        "cflags_cc": [
            "-std=c++2a"
        ],
        "conditions": [
            [ 'OS=="mac"',
                { "xcode_settings": {
                    'OTHER_CPLUSPLUSFLAGS' : ['-std=c++20','-stdlib=libc++','-Wno-deprecated-declarations'],
                    'OTHER_LDFLAGS': ['-stdlib=libc++'],
                    'MACOSX_DEPLOYMENT_TARGET': '10.15'
                }}
            ]
        ]
    }]
}
