rule auto_rule_20250726070029_5728 {
  strings:
    $o0 = "CharUpperBuffW" wide ascii nocase
    $o1 = "ptScreen" wide ascii nocase
    $o2 = "lpMenuTemplate" wide ascii nocase
    $o3 = "EnumPropsA" wide ascii nocase
    $o4 = "idItem" wide ascii nocase
  condition:
    4 of ($o*)
}