rule auto_rule_20250726134509_8369 {
  strings:
    $o0 = "dword_592FF0" wide ascii nocase
    $o1 = "x4E4" wide ascii nocase
    $o2 = "xA51" wide ascii nocase
    $o3 = "byte_509152" wide ascii nocase
    $o4 = "x7C0" wide ascii nocase
  condition:
    4 of ($o*)
}