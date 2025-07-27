rule auto_rule_20250726094640_9689 {
  strings:
    $o0 = "dword_44A044" wide ascii nocase
    $o1 = "_byte_0" wide ascii nocase
  condition:
    all of them
}