rule auto_rule_20250726085628_9131 {
  strings:
    $o0 = "CharUpperA" wide ascii nocase
    $o1 = "GetListBoxInfo" wide ascii nocase
    $o2 = "LoadMenuW" wide ascii nocase
    $o3 = "uFormat" wide ascii nocase
  condition:
    4 of ($o*)
}