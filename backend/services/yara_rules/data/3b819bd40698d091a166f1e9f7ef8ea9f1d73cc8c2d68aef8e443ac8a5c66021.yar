rule auto_rule_20250726171432_9213 {
  strings:
    $o0 = "DeleteMenu" wide ascii nocase
    $o1 = "flProtect" wide ascii nocase
    $o2 = "ptScreen" wide ascii nocase
    $o3 = "aClassesClsid0d" wide ascii nocase
    $o4 = "idChild" wide ascii nocase
  condition:
    4 of ($o*)
}