rule auto_rule_20250726205148_8151 {
  strings:
    $o0 = "lpCharType" wide ascii nocase
    $o1 = "byte_4673C6" wide ascii nocase
    $o2 = "x157" wide ascii nocase
    $o3 = "CodePagea" wide ascii nocase
  condition:
    4 of ($o*)
}