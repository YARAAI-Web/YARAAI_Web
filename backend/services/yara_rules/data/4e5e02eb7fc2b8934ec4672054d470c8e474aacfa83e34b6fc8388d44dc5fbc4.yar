rule auto_rule_20250726135846_4558 {
  strings:
    $o0 = "lpExtension" wide ascii nocase
    $o1 = "dwLowBytesToSeek" wide ascii nocase
    $o2 = "uIDNewItem" wide ascii nocase
    $o3 = "nMaxInstances" wide ascii nocase
  condition:
    4 of ($o*)
}