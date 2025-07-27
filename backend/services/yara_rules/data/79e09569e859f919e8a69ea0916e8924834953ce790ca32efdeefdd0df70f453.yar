rule auto_rule_20250726113308_5325 {
  strings:
    $o0 = "TrailDown1_0" wide ascii nocase
    $o1 = "dword_445EE4" wide ascii nocase
    $o2 = "TrailUp3" wide ascii nocase
    $o3 = "__crtMessageBoxA" wide ascii nocase
    $o4 = "byte_446181" wide ascii nocase
  condition:
    4 of ($o*)
}