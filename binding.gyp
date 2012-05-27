{
  'targets': [
    {
      'target_name': 'DTraceProviderBindings',
      'sources': [
	'dtrace_provider.cc',
	'dtrace_dof.cc',
      ],
      'conditions': [
	[ 'OS=="mac"', { 'sources': ['darwin-x86_64/drtace_probe.cc'] }], 
	[ 'OS=="solaris"', {'sources': ['solaris-i386/dtrace_probe.cc'] }],
      ],
      'defines': [
	'compiler_cxx',
	'CXXFLAGS',
	'-D_HAVE_DTRACE',
      ],
    }
  ]
}
