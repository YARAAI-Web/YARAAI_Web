rule auto_rule_20250726144947_1350 {
  strings:
    $o0 = "dword_781F8" wide ascii nocase
    $o1 = "byte_1E878" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}