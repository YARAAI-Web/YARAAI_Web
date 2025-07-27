rule auto_rule_20250726094915_6347 {
  strings:
    $o0 = "dword_46060C" wide ascii nocase
    $o1 = "LibraryA" wide ascii nocase
    $o2 = "doexit" wide ascii nocase
  condition:
    3 of ($o*)
}