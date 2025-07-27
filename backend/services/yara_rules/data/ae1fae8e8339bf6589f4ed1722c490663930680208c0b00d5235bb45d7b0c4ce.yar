rule auto_rule_20250726063049_6939 {
  strings:
    $o0 = "hcur" wide ascii nocase
    $o1 = "lpOutputFunc" wide ascii nocase
    $o2 = "lprc" wide ascii nocase
    $o3 = "CharUpperBuffW" wide ascii nocase
    $o4 = "MapVirtualKeyA" wide ascii nocase
  condition:
    5 of ($o*)
}