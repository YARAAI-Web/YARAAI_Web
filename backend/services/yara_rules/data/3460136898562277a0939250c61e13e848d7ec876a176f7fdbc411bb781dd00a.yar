rule auto_rule_20250726152500_3056 {
  strings:
    $o0 = "aPngtwlfj" wide ascii nocase
    $o1 = "byte_7365C" wide ascii nocase
    $o2 = "dword_783D4" wide ascii nocase
    $o3 = "dword_78114" wide ascii nocase
    $o4 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}