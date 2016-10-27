/*
This demo visualises wine and cheese pairings.
*/

$(function(){

  var layoutPadding = 50;
  var layoutDuration = 500;

  // get exported json from cytoscape desktop via ajax
  var graphP = $.ajax({
    url: 'graph.json', // wine-and-cheese.json
    type: 'GET',
    dataType: 'json'
  });

  // also get style via ajax
  var styleP = $.ajax({
    url: 'style.raw', // wine-and-cheese-style.cycss
    type: 'GET',
    dataType: 'text'
  });
  
  var infoTemplate = Handlebars.compile([
    '<p class="ac-name">{{name}}</p>',
    '<p class="ac-node-type"><i class="fa fa-info-circle"></i> {{category}} {{#if lang}}({{lang}}){{/if}}</p>',
    '{{#if shodan_ip}}',
    '{{#each shodan_ip}}<p class="ac-node-type">{{shodan_ip}}</p>{{/each}}',
    '{{/if}}',
    '{{#if shodan_keyssh}}<p class="ac-node-type">{{shodan_keyssh}}</p>{{/if}}',
    '<p class="ac-more"><i class="fa fa-external-link"></i> <a target="_blank" href="https://duckduckgo.com/?q={{name}}">More information</a></p>'
  ].join(''));

  // when both graph export json and style loaded, init cy
  Promise.all([ graphP, styleP ]).then(initCy);

  function highlight( node ){
    var nhood = node.closedNeighborhood();

    cy.batch(function(){
      cy.elements().not( nhood ).removeClass('highlighted').addClass('faded');
      nhood.removeClass('faded').addClass('highlighted');
      
      var npos = node.position();
      var w = window.innerWidth;
      var h = window.innerHeight;
      
      /*cy.stop().animate({
        fit: {
          eles: cy.elements(),
          padding: layoutPadding
        }
      }, {
        duration: layoutDuration
      }).delay( layoutDuration, function(){
        nhood.layout({
          name: 'concentric',
          padding: layoutPadding,
          animate: true,
          animationDuration: layoutDuration,
          boundingBox: {
            x1: npos.x - w/2,
            x2: npos.x + w/2,
            y1: npos.y - w/2,
            y2: npos.y + w/2
          },
          fit: true,
          concentric: function( n ){
            if( node.id() === n.id() ){
              return 2;
            } else {
              return 1;
            }
          },
          levelWidth: function(){
            return 1;
          }
        });
      } );*/
      
    });
  }

  function clear(){
    cy.batch(function(){
      cy.$('.highlighted').forEach(function(n){
        n.animate({
          position: n.data('orgPos')
        });
      });
      
      cy.elements().removeClass('highlighted').removeClass('faded');
    });
  }

  function showNodeInfo( node ){
    $('#info').html( infoTemplate( node.data() ) ).show();
  }
  
  function hideNodeInfo(){
    $('#info').hide();
  }

  function initCy( then ){
    var loading = document.getElementById('loading');
    var expJson = then[0];
    var styleJson = then[1];
    var elements = expJson.elements;

    elements.nodes.forEach(function(n){
      var data = n.data;
      
      /*n.data.orgPos = {
        x: n.position.x,
        y: n.position.y
      };*/
    });

    loading.classList.add('loaded');

    var cy = window.cy = cytoscape({
      container: document.getElementById('cy'),
      layout: { name: 'grid', padding: 10 },
      style: styleJson,
      elements: elements,
      motionBlur: true,
      selectionType: 'single',
      boxSelectionEnabled: false,
      autoselectify: true,
    });
    
    /*cy.on('free', 'node', function( e ){
      var n = e.cyTarget;
      var p = n.position();
      
      n.data('orgPos', {
        x: p.x,
        y: p.y
      });
    });*/
    
    cy.on('tap', function(){
      $('#search').blur();
    });

    cy.on('select', 'node', function(e){
      var node = this;

      highlight( node );
      showNodeInfo( node );
    });

    cy.on('unselect', 'node', function(e){
      var node = this;

      clear();
      hideNodeInfo();
    });

  }
  
  $('#search').typeahead({
    minLength: 2,
    highlight: true,
  },
  {
    name: 'search-dataset',
    source: function( query, cb ){
      function matches( str, q ){
        str = (str || '').toLowerCase();
        q = (q || '').toLowerCase();
        
        return str.match( q );
      }
      
      var fields = ['name'];
      
      function anyFieldMatches( n ){
        for( var i = 0; i < fields.length; i++ ){
          var f = fields[i];
          
          if( matches( n.data(f), query ) ){
            return true;
          }
        }
        
        return false;
      }
      
      function getData(n){
        var data = n.data();
        
        return data;
      }
      
      function sortByName(n1, n2){
        if( n1.data('name') < n2.data('name') ){
          return -1;
        } else if( n1.data('name') > n2.data('name') ){
          return 1;
        }
        
        return 0;
      }
      
      var res = cy.nodes().stdFilter( anyFieldMatches ).sort( sortByName ).map( getData );
      
      cb( res );
    },
    templates: {
      suggestion: infoTemplate
    }
  }).on('typeahead:selected', function(e, entry, dataset){
    var n = cy.getElementById(entry.id);
    
    n.select();
    showNodeInfo( n );
  });
  
  $('#reset').on('click', function(){
    cy.animate({
      fit: {
        eles: cy.elements(),
        padding: layoutPadding
      },
      duration: layoutDuration
    });
  });
  
  $('#filters').on('click', 'input', function(){
     
    // category
    var weapons = $('#weapons').is(':checked');
    var humans = $('#humans').is(':checked');
    var drugs = $('#drugs').is(':checked');
    var papers = $('#papers').is(':checked');
    var mafia = $('#mafia').is(':checked');
    var money = $('#money').is(':checked');
    var art = $('#art').is(':checked');
    var pedophilia = $('#pedophilia').is(':checked');
    var organs = $('#organs').is(':checked');
    var techs = $('#techs').is(':checked');
    var animals = $('#animals').is(':checked');
    var islamist = $('#islamist').is(':checked');
    var prostitution = $('#prostitution').is(':checked');
    var porn = $('#porn').is(':checked');

    // lang
    var fr = $('#fr').is(':checked');
    var en = $('#en').is(':checked');
    var de = $('#de').is(':checked');
    var es = $('#es').is(':checked');
    var ru = $('#ru').is(':checked');
    
    cy.batch(function(){
      
      cy.nodes().forEach(function( n ){
        var type = n.data('category');
        var type_lang = n.data('lang');
        
        n.removeClass('filtered');
        
        var filter = function(){
          n.addClass('filtered');
        };
        
        if( type === 'weapons' ){

          if( !weapons ){ filter(); };

        } else if( type === 'humans' ){

          if( !humans ){ filter(); };

        } else if( type === 'drugs' ){

          if( !drugs ){ filter(); };

        } else if( type === 'papers' ){

          if( !papers ){ filter(); };

        } else if( type === 'mafia' ){

          if( !mafia ){ filter(); };

        } else if( type === 'money' ){

          if( !money ){ filter(); };

        } else if( type === 'art' ){

          if( !art ){ filter(); };

        } else if( type === 'pedophilia' ){

          if( !pedophilia ){ filter(); };

        } else if( type === 'organs' ){

          if( !organs ){ filter(); };

        } else if( type === 'techs' ){

          if( !techs ){ filter(); };

        } else if( type === 'animals' ){

          if( !animals ){ filter(); };

        } else if( type === 'islamist' ){

          if( !islamist ){ filter(); };

        } else if( type === 'islamist' ){

          if( !protitution ){ filter(); };

        } else if( type === 'porn' ){

          if( !porn ){ filter(); };

        }


        if( type_lang === 'fr' ){

          if( !fr ){ filter(); };

        } else if( type_lang === 'en' ){

          if( !en ){ filter(); };

        } else if( type_lang === 'de' ){

          if( !de ){ filter(); };

        } else if( type_lang === 'es' ){

          if( !es ){ filter(); };

        } else if( type_lang === 'ru' ){

          if( !ru ){ filter(); };

        }

      });
      
    });
    
  });
  
  $('#filter').qtip({
    position: {
      my: 'top center',
      at: 'bottom center'
    },
    
    show: {
      event: 'click'
    },
    
    hide: {
      event: 'unfocus'
    },
    
    style: {
      classes: 'qtip-bootstrap',
      tip: {
        width: 16,
        height: 8
      }
    },

    content: $('#filters')
  });
});
