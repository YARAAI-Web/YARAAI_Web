rule auto_rule_20250726220257_2945 {
  strings:
    $o0 = "IsCharLowerW" wide ascii nocase
    $o1 = "pblend" wide ascii nocase
    $o2 = "fByPositon" wide ascii nocase
    $o3 = "WOWShellExecute" wide ascii nocase
    $o4 = "CompletionKey" wide ascii nocase
  condition:
    4 of ($o*)
}