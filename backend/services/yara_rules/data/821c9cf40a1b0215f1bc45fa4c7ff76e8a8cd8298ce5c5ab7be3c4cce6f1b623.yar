rule auto_rule_20250726191628_8294 {
  strings:
    $o0 = "BroadcastSystemMessageA" wide ascii nocase
    $o1 = "CreateIconFromResource" wide ascii nocase
    $o2 = "UnpackDDElParam" wide ascii nocase
    $o3 = "nMaxCount" wide ascii nocase
    $o4 = "cchItemText" wide ascii nocase
  condition:
    4 of ($o*)
}