rule auto_rule_20250726091840_9919 {
  strings:
    $o0 = "DllMain" wide ascii nocase
    $o1 = "MenuState" wide ascii nocase
    $o2 = "off_101196FC" wide ascii nocase
  condition:
    3 of ($o*)
}