rule auto_rule_20250727043536_2257 {
  strings:
    $o0 = "cause" wide ascii nocase
    $o1 = "copy_start" wide ascii nocase
    $o2 = "xDAE9B268" wide ascii nocase
    $o3 = "lpCharType" wide ascii nocase
    $o4 = "_getptd" wide ascii nocase
  condition:
    5 of ($o*)
}